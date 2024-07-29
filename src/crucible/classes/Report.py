import json
import time


class Report:
    def __init__(self, runner):
        self.name = runner.id
        self.models = [x.id for x in runner.models]
        self.prompts = [x.id for x in runner.prompts]
        self.variables = [x.id for x in runner.variables]

        self.n_cases = len(runner.tasks)

        self.cost = round(runner.calculate_costs(), 2)
        self.time = round(time.perf_counter() - runner.start_time, 1)

        self.tasks = self._generate_tasks_report(runner)

        self.per_model = self._by_category(runner, "models", "model")
        self.per_prompt = self._by_category(runner, "prompts", "prompt")
        self.per_variable = self._by_category(runner, "variables", "variable")

    def _generate_tasks_report(self, runner):
        tasks_report = []
        for task in runner.tasks:
            task_info = {
                "grade": task.result.grade if task.result else "NULL",
                "info": task.result.info if task.result else "NULL",
                "model": task.model.id,
                "prompt": task.prompt.id,
                "variable": task.variable.id,
            }
            tasks_report.append(task_info)
        return tasks_report

    def log_report(self):
        with open(f"output/{self.name}.json", "w") as f:
            json.dump(self.__dict__, f)

    def _by_category(self, runner, attr1, attr2) -> list:
        vars = []
        for item in getattr(runner, attr1):
            tasks_with_variable = [
                task for task in runner.tasks if getattr(task, attr2).id == item.id
            ]

            sum_grades = sum(
                task.result.grade
                for task in tasks_with_variable
                if task.result is not None
            )

            MAX_GRADE = 10
            total_max_grade = MAX_GRADE * len(tasks_with_variable)

            info = {
                "name": item.id,
                "grade": sum_grades,
                "total_grade": total_max_grade,
                "percentage": f"{sum_grades / total_max_grade * 100:.2f}%",
            }
            vars.append(info)
        return vars
