import uuid
import time

from crucible.prompts import prompts_
from crucible.variables import variables_
from crucible.models import models_
from crucible.classes.Report import Result
from crucible.utils.grading import GradingType
from crucible.classes.Printer import Printer
from crucible.classes.Task import Task

from crucible.utils.grading import grade_response
from crucible.utils.validation import check_exists
from crucible.utils.io import load_models, load_prompts, load_variables

GRADING_TYPE = GradingType.QUALITATIVE  # qualitative uses gpt4o; use with care.
TEMPERATURE = 0.0
DANGER_MODE = True  # does not ask permission about prices; use with care.


def main():
    run_id = time.strftime("%Y%m%d%H%M%S")
    title = f"CRUCIBLE PROMPT EVALUATION {run_id}"

    MODELS = load_models(models_)
    PROMPTS = load_prompts(prompts_)
    VARIABLES = load_variables(variables_)

    check_exists(MODELS, PROMPTS, VARIABLES)

    printer = Printer(title, MODELS, PROMPTS, VARIABLES, GRADING_TYPE)
    printer.start()

    tasks = []
    for model in MODELS:
        for prompt in PROMPTS:
            for variable in VARIABLES:

                task = Task(
                    run_id=run_id,
                    task_id=uuid.uuid4().hex,
                    model=model,
                    prompt=prompt,
                    variable=variable,
                    expected=variable.expected,
                )

                tasks.append(task)

    printer.calculate_costs_all(tasks, DANGER_MODE)
    printer.print_header()

    for task in tasks:
        try:
            start_query_time = time.perf_counter()
            response = model.query(prompt, variable, TEMPERATURE, DANGER_MODE)
            grade, info = grade_response(response, variable, GRADING_TYPE)

            result = Result(
                task=task,
                response=response,
                grade=grade,
                info=info,
                time_elapsed=round(time.perf_counter() - start_query_time, 2),
            )

        except Exception as e:
            result = Result(
                task=task,
                response=None,
                grade=None,
                info=None,
                time_elapsed=round(time.perf_counter() - start_query_time, 2),
                error=str(e),
            )

        finally:
            printer.print_result(result)
            printer.report.results.append(result)
            printer.save_report(run_id)

    printer.print_report(run_id)
    printer.compute_time()
    print()


if __name__ == "__main__":
    main()
