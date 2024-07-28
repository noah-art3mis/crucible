import time
import uuid

from crucible.classes.Model import Model
from crucible.classes.Task import Task
from crucible.classes.Report import Result, Report
from crucible.classes.Variable import Variable
from crucible.classes.Prompt import Prompt
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
    ):
        self._check_exists(models, prompts, variables)

        self.models = models
        self.prompts = prompts
        self.variables = variables
        self.grading_type = grading_type
        self.danger_mode = danger_mode
        self.temp = temperature

        self.id = time.strftime("%Y%m%d%H%M%S")
        self.tasks = self._generate_tasks(models, prompts, variables)
        self.report = Report()
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

            response = task.model.query(
                task.prompt,
                task.variable,
                self.temp,
                self.danger_mode,
            )

            grade, info = grade_response(
                response,
                task.variable,
                self.grading_type,
            )

            task.result = Result(
                response=response,
                grade=grade,
                info=info,
                actual_cost=task.model.calculate_cost(response),
                time_elapsed=round(time.perf_counter() - start_query_time, 2),
            )

        except Exception as e:
            print(f"Error with task {task.id}: {e}")
            task.result = Result(
                response=None,
                grade=0,
                info=str(e),
                actual_cost=None,
                time_elapsed=round(time.perf_counter() - start_query_time, 2),
            )

    def estimate_all_costs(self, danger_mode: bool = False) -> None:
        total_cost = 0.0
        for task in self.tasks:
            total_cost += task.estimated_cost

        are_you_sure(total_cost, danger_mode)

    def _check_exists(self, *args) -> None:
        for arg in args:
            if arg is None:
                raise ValueError(f"No globals provided for {arg}")
