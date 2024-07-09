import re
from utils.my_types import BaseEntity, Model, Prompt, Variable, Result, Report
from utils.grading import GradingType
import copy


class Runner:

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

    def start(self):
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
            self.report.header += item
        print()

    def print_header(self):

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

    def print_result(self, result: Result):
        padding = 1
        max_chars = 100

        case = f"{self.current_case}/{self.total_cases}"
        info = result.info if result.info is not None else ""
        info = info[:max_chars] + "..."

        max_widths = {
            case: len("99/99"),
            str(result.grade): len("grade"),
            result.model_id: self._get_len("model", self.models),
            result.prompt_id: self._get_len("prompt", self.prompts),
            result.variable_id: self._get_len("variable", self.variables),
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

    def print_report(self):
        print("\nREPORT\n")
        self._model_report()
        self._prompt_report()
        self._variable_report()

    def _model_report(self):
        print("BY MODEL")
        for model in self.models:
            models = [x for x in self.report.results if x.model_id == model.id]
            self._partial_result(model.id, models)

    def _prompt_report(self):
        print("BY PROMPT")
        for prompt in self.prompts:
            prompts = [x for x in self.report.results if x.prompt_id == prompt.id]
            self._partial_result(prompt.id, prompts)

    def _variable_report(self):
        print("BY VARIABLE")
        for variable in self.variables:
            variables = [x for x in self.report.results if x.variable_id == variable.id]
            self._partial_result(variable.id, variables)

    def _partial_result(self, name: str, cases: list[Result]):
        MAX_GRADE = 10
        total_max_grade = MAX_GRADE * len(cases)
        sum_grades = sum(x.grade for x in cases if x.grade is not None)
        percentage = sum_grades / total_max_grade
        print(f"\t{name}: {sum_grades}/{total_max_grade} ({percentage * 100:.0f}%)")
