import uuid
import time

import ollama

from eval_prompts import prompts
from eval_variables import variables
from eval_models import models
from utils.my_types import Result
from utils.grading import GradingType
from utils.runner import Runner

from utils.llm import query
from utils.grading import grade_response
from utils.validation import check_exists
from utils.io import save_logs

MODELS = models
PROMPTS = prompts
VARIABLES = variables
TEMPERATURE = 0.0
DANGER_MODE = True  # does not ask permission about prices; use with care.
GRADING_TYPE = GradingType.QUALITATIVE  # qualitative uses gpt4o; use with care.


def main():
    start_time = time.perf_counter()
    run_id = time.strftime("%Y%m%d%H%M%S")
    title = f"CRUCIBLE PROMPT EVALUATION {run_id}"

    check_exists(MODELS, PROMPTS, VARIABLES)

    runner = Runner(title, MODELS, PROMPTS, VARIABLES, GRADING_TYPE)
    runner.start()
    runner.print_header()

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
                    response = query(model, prompt, variable, TEMPERATURE, DANGER_MODE)
                    grade, info = grade_response(response, variable, GRADING_TYPE)

                    result.response = response
                    result.grade = grade
                    result.info = info

                    runner.print_result(result)

                except ollama.ResponseError as e:
                    result.response = response
                    result.grade = 0
                    result.time_elapsed = _time
                    result.error = e.error
                    print("Error:", e.error)

                finally:
                    _time = round(time.perf_counter() - start_query_time, 2)
                    result.time_elapsed = _time
                    runner.report.results.append(result)
                    save_logs(runner.report, run_id)

    runner.print_report()
    print(f"Time taken: {time.perf_counter() - start_time:.0f} seconds")
    print(f"Saved logs to: outputs/{run_id}")


if __name__ == "__main__":
    main()
