import uuid
import time

from crucible.prompts import prompts_
from crucible.variables import variables_
from crucible.models import models_
from crucible.utils.my_types import Result
from crucible.utils.grading import GradingType
from crucible.utils.Printer import Printer

from crucible.utils.grading import grade_response
from crucible.utils.validation import check_exists
from crucible.utils.io import save_logs, load_models, load_prompts, load_variables

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
    printer.print_header()

    for model in MODELS:
        for prompt in PROMPTS:
            for variable in VARIABLES:
                start_query_time = time.perf_counter()

                result = Result(
                    run_id=run_id,
                    case_id=uuid.uuid4().hex,
                    model_id=model.id,
                    prompt_id=prompt.id,
                    variable_id=variable.id,
                    expected=variable.expected,
                )

                try:
                    response = model.query(prompt, variable, TEMPERATURE, DANGER_MODE)
                    grade, info = grade_response(response, variable, GRADING_TYPE)

                    result.response = response
                    result.grade = grade
                    result.info = info

                    printer.print_result(result)

                finally:
                    _time = round(time.perf_counter() - start_query_time, 2)
                    result.time_elapsed = _time
                    printer.report.results.append(result)
                    printer.save_report(run_id)

    printer.print_report()
    printer.compute_time()
    print()


if __name__ == "__main__":
    main()
