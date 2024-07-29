from crucible.classes.Model import Model
from crucible.classes.Prompt import Prompt
from crucible.classes.Variable import Variable
from crucible.classes.Result import Result
from crucible.classes.Runner import Runner
from crucible.classes.Task import Task
from crucible.classes.Report import Report

import time


class Printer:
    def __init__(self, runner: Runner) -> None:
        self.runner = runner
        self.current_case = 1

    def display_start(self) -> None:
        content = []
        title = f"CRUCIBLE PROMPT EVALUATION {self.runner.id}"

        content.append("=" * len(title))
        content.append(title)
        content.append("=" * len(title))
        content.append(f"models: " + ", ".join([str(x.id) for x in self.runner.models]))
        content.append(
            f"prompts: " + ", ".join([str(x.id) for x in self.runner.prompts])
        )
        content.append(
            f"variables: " + ", ".join([str(x.id) for x in self.runner.variables])
        )
        content.append(
            f"total cases: {len(self.runner.models) * len(self.runner.prompts) * len(self.runner.variables)}"
        )
        content.append("=" * len(title))

        for item in content:
            print(item)
        print()

    def display_header(self) -> None:

        max_widths = {
            "case": len("99/99"),
            "grade": len("grade"),
            "model": self._get_len("model", self.runner.models),
            "prompt": self._get_len("prompt", self.runner.prompts),
            "variable": self._get_len("variable", self.runner.variables),
            "info": len("info"),
        }

        padding = 1
        results = (x.ljust(max_widths[x] + padding) for x in max_widths)
        header = "| ".join(results)
        print(header)

    def display_result(self, task: Task) -> None:
        padding = 1
        max_chars = 100
        result: Result | None = task.result

        if result is None:
            raise ValueError("Result cannot be None")

        case = f"{self.current_case}/{len(self.runner.tasks)}"
        info = result.info if result.info is not None else ""
        info = info[:max_chars] + "..."

        max_widths = {
            case: len("99/99"),
            str(result.grade): len("grade"),
            task.model.id: self._get_len("model", self.runner.models),
            task.prompt.id: self._get_len("prompt", self.runner.prompts),
            task.variable.id: self._get_len("variable", self.runner.variables),
            info: len("info"),
        }

        results = (x.ljust(max_widths[x] + padding) for x in max_widths)
        data = "| ".join(results)

        self.current_case += 1
        print(data)

    def _get_len(
        self, category_name: str, var: list[Model] | list[Prompt] | list[Variable]
    ) -> int:
        largest_name_in_list = max(len(str(x.id)) for x in var)
        return max(len(category_name), largest_name_in_list)

    def display_price(self) -> None:
        costs = self.runner.calculate_costs()
        print(f"Actual costs: ${costs:.2f}")

    def display_report(self) -> None:
        print("\nREPORT\n")

        print("BY MODEL")
        model_grades = self._model_report()
        for item in model_grades:
            print(f"{item[0]}: {item[1]} / {item[2]} ({item[1] / item[2] * 100:.2f}%)")

        print("BY PROMPT")
        prompt_grades = self._prompt_report()
        for item in prompt_grades:
            print(f"{item[0]}: {item[1]} / {item[2]} ({item[1] / item[2] * 100:.2f}%)")

        print("BY VARIABLE")
        variable_grades = self._variable_report()
        for item in variable_grades:
            print(f"{item[0]}: {item[1]} / {item[2]} ({item[1] / item[2] * 100:.2f}%)")

        print()
        self.display_price()
        self.display_elapsed_time()
        print(f"Saved logs to: outputs/{self.runner.id}")

    def _model_report(self) -> list[tuple[str, int, int]]:
        grading = []
        for model in self.runner.models:
            tasks_with_model = [x for x in self.runner.tasks if x.model.id == model.id]
            grades, total_grades = self._results_by(tasks_with_model)
            grading.append((model.id, grades, total_grades))
        return grading

    def _prompt_report(self) -> list[tuple[str, int, int]]:
        grading = []
        for prompt in self.runner.prompts:
            tasks_with_prompt = [
                x for x in self.runner.tasks if x.prompt.id == prompt.id
            ]
            grades, total_grades = self._results_by(tasks_with_prompt)
            grading.append((prompt.id, grades, total_grades))
        return grading

    def _variable_report(self) -> list[tuple[str, int, int]]:
        grading = []
        for variable in self.runner.variables:
            tasks_with_variable = [
                x for x in self.runner.tasks if x.variable.id == variable.id
            ]
            grades, total_grades = self._results_by(tasks_with_variable)
            grading.append((variable.id, grades, total_grades))
        return grading

    def _results_by(self, cases: list[Task]) -> tuple[int, int]:
        MAX_GRADE = 10

        sum_grades = sum(x.result.grade for x in cases if x.result is not None)

        total_max_grade = MAX_GRADE * len(cases)
        return sum_grades, total_max_grade

    def display_elapsed_time(self) -> None:
        t = time.perf_counter() - self.runner.start_time
        print(f"Time elapsed: {t:.1f}s\n")
