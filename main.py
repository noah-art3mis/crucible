import uuid
import time

import ollama

from eval_prompts import prompts
from eval_variables import variables
from eval_models import models

from utils.my_types import Result

from utils.llm import query
from utils.grading import grade_response
from utils.display import print_data, generate_and_show_summary
from utils.validation import check_exists
from utils.io import save_logs


MODELS = models
PROMPTS = prompts
VARIABLES = variables
TEMPERATURE = 0.0
GRADING_TYPE = "out_of_ten"


def main():
    start_time = time.perf_counter()
    run_id = time.strftime("%Y%m%d%H%M%S")

    print()
    print(f"CRUCIBLE PROMPT EVALUATION {run_id}")
    print()
    print(f"models: " + ", ".join([str(x.id) for x in MODELS]))
    print(f"prompts: " + ", ".join([str(x.id) for x in PROMPTS]))
    print(f"variables: " + ", ".join([str(x.id) for x in VARIABLES]))
    total_cases = len(MODELS) * len(PROMPTS) * len(VARIABLES)
    print(f"total cases: {total_cases}")
    print()

    check_exists(MODELS, PROMPTS, VARIABLES)

    print_data(
        "case",
        "model",
        "prompt",
        "variable",
        "case_id",
        "grade",
        MODELS,
        PROMPTS,
        VARIABLES,
    )

    outputs: list[Result] = []
    counter = 0
    for model in MODELS:
        for prompt in PROMPTS:
            for variable in VARIABLES:
                start_query_time = time.perf_counter()
                case_id = uuid.uuid4().hex
                result = Result(
                    id=case_id,
                    model=model.id,
                    prompt_id=prompt.id,
                    variable_id=variable.id,
                    expected=variable.expected,
                )

                try:
                    output = query(model, prompt, variable, TEMPERATURE)
                    response = output["message"]["content"]  # type: ignore
                    grade = grade_response(response, variable, GRADING_TYPE)

                    result.response = response
                    result.grade = grade

                    print_data(
                        f"{counter}/{total_cases}",
                        model.id,
                        prompt.id,
                        variable.id,
                        case_id,
                        str(grade),
                        MODELS,
                        PROMPTS,
                        VARIABLES,
                    )

                except ollama.ResponseError as e:
                    result.response = response
                    result.grade = 0
                    result.time_elapsed = _time
                    result.error = e.error
                    print("Error:", e.error)

                finally:
                    _time = round(time.perf_counter() - start_query_time, 2)
                    result.time_elapsed = _time
                    outputs.append(result)
                    save_logs(outputs, run_id)
                    counter += 1

    print()
    print("SUMMARY")
    print()
    print("BY MODEL")
    generate_and_show_summary(outputs, MODELS)
    print()
    print("BY PROMPT")
    generate_and_show_summary(outputs, PROMPTS)
    print()
    print("BY VARIABLE")
    generate_and_show_summary(outputs, VARIABLES)
    print()
    print("BY EXPECTED")
    print("todo")
    # generate_and_show_summary(outputs, VARIABLES)
    print()
    print(f"Time taken: {time.perf_counter() - start_time:.0f} seconds")
    print(f"Saved logs to: outputs/{run_id}")


if __name__ == "__main__":
    main()
