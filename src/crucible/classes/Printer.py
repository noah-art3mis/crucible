import sys
import time
import yaml
from crucible.classes.Model import Model
from crucible.classes.Task import Task
from crucible.utils.grading import GradingType
from crucible.classes.Report import Result, Report
from crucible.classes.Variable import Variable
from crucible.classes.Prompt import Prompt


class Printer:

    def __init__(
        self,
        title: str,
        models: list[Model],
        prompts: list[Prompt],
        variables: list[Variable],
        grading_type: GradingType,
    ):
        self.title = title
        self.models = models
        self.prompts = prompts
        self.variables = variables
        self.total_cases = len(self.models) * len(self.prompts) * len(self.variables)
        self.current_case = 1
        self.report = Report()
        self.grading_type = grading_type
        self.start_time = time.perf_counter()

    def start(self) -> None:
        content = []

        content.append("\n")
        content.append("=" * len(self.title))
        content.append(self.title)
        content.append("=" * len(self.title))
        content.append(f"models: " + ", ".join([str(x.id) for x in self.models]))
        content.append(f"prompts: " + ", ".join([str(x.id) for x in self.prompts]))
        content.append(f"variables: " + ", ".join([str(x.id) for x in self.variables]))
        content.append(
            f"total cases: {len(self.models) * len(self.prompts) * len(self.variables)}"
        )
        content.append("=" * len(self.title))

        for item in content:
            print(item)
            self.report.header += item + "\n"
        print()

    def print_header(self) -> None:

        max_widths = {
            "case": len("99/99"),
            "grade": len("grade"),
            "model": self._get_len("model", self.models),
            "prompt": self._get_len("prompt", self.prompts),
            "variable": self._get_len("variable", self.variables),
            "info": len("info"),
        }

        padding = 1
        results = (x.ljust(max_widths[x] + padding) for x in max_widths)
        header = "| ".join(results)
        print(header)

    def calculate_costs_all(self, tasks: list[Task], danger_mode: bool = False) -> None:
        total_cost = 0.0
        for task in tasks:
            messages = task.model.build_messages(task.prompt, task.variable)
            n_tokens = task.model.get_n_tokens(str(messages))
            task_cost = task.model.estimate_costs(n_tokens)
            total_cost += task_cost

        if not danger_mode:
            if not self._ask_permission(total_cost):
                sys.exit(0)

    def print_result(self, result: Result) -> None:
        padding = 1
        max_chars = 100

        case = f"{self.current_case}/{self.total_cases}"
        info = result.info if result.info is not None else ""
        info = info[:max_chars] + "..."

        max_widths = {
            case: len("99/99"),
            str(result.grade): len("grade"),
            result.task.model.id: self._get_len("model", self.models),
            result.task.prompt.id: self._get_len("prompt", self.prompts),
            result.task.variable.id: self._get_len("variable", self.variables),
            info: len("info"),
        }

        results = (x.ljust(max_widths[x] + padding) for x in max_widths)
        data = "| ".join(results)

        self.current_case += 1
        print(data)

    def print_report(self, run_id: str) -> None:
        print("\nREPORT\n")
        self._model_report()
        self._prompt_report()
        self._variable_report()
        print(f"Saved logs to: outputs/{run_id}")

    def compute_time(self) -> None:
        print(f"Time elapsed: {time.perf_counter() - self.start_time:.0f} seconds")

    def save_report(self, run_id: str) -> None:
        with open(f"outputs/{run_id}.yaml", "w", encoding="utf-8") as f:
            yaml.dump(
                self.report.results, f, indent=2, allow_unicode=True, sort_keys=False
            )

    def _get_len(
        self, category_name: str, var: list[Model] | list[Prompt] | list[Variable]
    ) -> int:
        largest_name_in_list = max(len(str(x.id)) for x in var)
        return max(len(category_name), largest_name_in_list)

    def _model_report(self) -> None:
        print("BY MODEL")
        for model in self.models:
            models = [x for x in self.report.results if x.task.model.id == model.id]
            self._partial_result(model.id, models)

    def _prompt_report(self) -> None:
        print("BY PROMPT")
        for prompt in self.prompts:
            prompts = [x for x in self.report.results if x.task.prompt.id == prompt.id]
            self._partial_result(prompt.id, prompts)

    def _variable_report(self) -> None:
        print("BY VARIABLE")
        for variable in self.variables:
            variables = [
                x for x in self.report.results if x.task.variable.id == variable.id
            ]
            self._partial_result(variable.id, variables)

    def _partial_result(self, name: str, cases: list[Result]) -> None:
        MAX_GRADE = 10
        total_max_grade = MAX_GRADE * len(cases)
        sum_grades = sum(x.grade for x in cases if x.grade is not None)
        percentage = sum_grades / total_max_grade
        print(f"\t{name}: {sum_grades}/{total_max_grade} ({percentage * 100:.0f}%)")

    def _ask_permission(self, total_cost: float) -> bool:
        while True:
            print(f"This will cost around ${total_cost:.2f}.")
            response = (
                input("Are you sure you want to continue? (y/n): ").strip().lower()
            )
            if response == "y":
                print("Permission granted. Continuing...")
                return True
            elif response == "n":
                print("Permission denied. Exiting...")
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
