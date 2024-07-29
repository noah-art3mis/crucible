import time
import uuid

from crucible.classes.Model import Model, Source
from crucible.classes.Task import Task
from crucible.classes.Result import Result
from crucible.classes.Variable import Variable
from crucible.classes.Prompt import Prompt
from crucible.classes.Report import Report
from crucible.utils.grading import GradingType
from crucible.utils.confirmation import are_you_sure
from crucible.utils.grading import grade_response


class Runner:

    def __init__(
        self,
        models: list[Model],
        prompts: list[Prompt],
        variables: list[Variable],
        grading_type: GradingType,
        danger_mode: bool,
        temperature: float,
        openai_api_key: str,
        anthropic_api_key: str,
    ):
        self._check_exists(models, prompts, variables)

        self.models = models
        self.prompts = prompts
        self.variables = variables
        self.grading_type = grading_type
        self.danger_mode = danger_mode
        self.temperature = temperature
        self.openai_api_key = openai_api_key
        self.anthropic_api_key = anthropic_api_key

        self.id = time.strftime("%Y%m%d%H%M%S")
        self.tasks = self._generate_tasks(models, prompts, variables)
        self.start_time = time.perf_counter()

    def _generate_tasks(
        self, models: list[Model], prompts: list[Prompt], variables: list[Variable]
    ) -> list[Task]:
        tasks = []
        for model in models:
            for prompt in prompts:
                for variable in variables:

                    task = Task(
                        id=uuid.uuid4().hex,
                        model=model,
                        prompt=prompt,
                        variable=variable,
                        expected=variable.expected,
                        result=None,
                    )

                    tasks.append(task)
        return tasks

    def run_task(self, task: Task) -> None:
        try:
            start_query_time = time.perf_counter()

            if task.model.source == Source.OPENAI:
                api_key = self.openai_api_key
            if task.model.source == Source.ANTHROPIC:
                api_key = self.anthropic_api_key
            if task.model.source == Source.LOCAL:
                pass

            response, cost = task.model.query(
                task.prompt,
                task.variable,
                self.temperature,
                api_key,
            )

            grade, info = grade_response(
                response, task.variable, self.grading_type, self.openai_api_key
            )

            task.result = Result(
                grade=grade,
                actual_cost=cost,
                response=response,
                info=info,
                time_elapsed=round(time.perf_counter() - start_query_time, 2),
            )

        except Exception as e:
            print(f"Error with task {task.id}: {e}")
            task.result = Result(
                response=None,
                grade=0,
                info=str(e),
                actual_cost=0,  # not true; errors still count towards total cost
                time_elapsed=round(time.perf_counter() - start_query_time, 2),
            )

    def estimate_all_costs(self) -> float:
        total_cost = 0.0
        for task in self.tasks:
            total_cost += task.estimated_cost

        are_you_sure(total_cost, self.danger_mode)

        return total_cost

    def calculate_costs(self) -> float:
        total_cost = 0.0
        for task in self.tasks:
            if task.result is None:
                raise ValueError(f"Task {task.id} has no result.")

            total_cost += task.result.actual_cost

        are_you_sure(total_cost, self.danger_mode)

        return total_cost

    def _check_exists(self, *args) -> None:
        for arg in args:
            if arg is None:
                raise ValueError(f"No globals provided for {arg}")

    def generate_report(self) -> str:
        for task in self.tasks:
            self.report.add_result(task)

        self.report.calculate_total_cost()

        return self.report.generate_report()
