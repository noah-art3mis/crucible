import uuid
import time
import yaml
import ollama
import time
from eval_prompts import prompts
from eval_variables import variables
from eval_models import models
from my_types import Result, Prompt, Variable, Model
from utils.llm import query
from utils.grading import grade_response
from utils.display import print_data, calculate_results
from utils.validation import check_exists

MODELS = models
PROMPTS = prompts
VARIABLES = variables
TEMPERATURE = 0.0


def main():
    start_time = time.perf_counter()
    run_id = time.strftime("%Y%m%d%H%M%S")

    print()
    print(f"CRUCIBLE PROMPT EVALUATION {run_id}")
    print()
    print(f"models: {[x.id for x in MODELS]}")
    print(f"models: " + ", ".join([str(x.id) for x in MODELS]))
    print(f"prompts: {[x.id for x in PROMPTS]}")
    print(f"prompts: " + ", ".join([str(x.id) for x in PROMPTS]))
    print(f"variables: {[x.id for x in VARIABLES]}")
    print(f"variables: " + ", ".join([str(x.id) for x in VARIABLES]))
    total_cases = len(MODELS) * len(PROMPTS) * len(VARIABLES)
    print(f"total cases: {total_cases}")
    print()

    check_exists(MODELS, PROMPTS, VARIABLES)

    print_data(
        "case", "model", "prompt", "variable", "grade", MODELS, PROMPTS, VARIABLES
    )

    outputs: list[Result] = []
    counter = 0
    for model in MODELS:
        for prompt in PROMPTS:
            for variable in VARIABLES:
                try:
                    start_query_time = time.perf_counter()
                    output = query(model, prompt, variable, TEMPERATURE)
                    response = output["message"]["content"]  # type: ignore
                    grade = grade_response(response, variable, grading_type="binary")

                    outputs.append(
                        Result(
                            id=uuid.uuid4().hex,
                            model=model.id,
                            prompt_id=prompt.id,
                            variable_id=variable.id,
                            expected=variable.expected,
                            response=response,
                            grade=grade,
                            time_elapsed=round(
                                time.perf_counter() - start_query_time, 2
                            ),
                            error=None,
                        )
                    )
                    counter += 1
                    print_data(
                        f"{counter}/{total_cases}",
                        model.id,
                        prompt.id,
                        variable.id,
                        str(grade),
                        MODELS,
                        PROMPTS,
                        VARIABLES,
                    )

                    with open(f"outputs/{run_id}.yaml", "w", encoding="utf-8") as f:
                        yaml.dump(
                            outputs, f, indent=2, allow_unicode=True, sort_keys=False
                        )

                except ollama.ResponseError as e:
                    outputs.append(
                        Result(
                            id=uuid.uuid4().hex,
                            model=model.id,
                            prompt_id=prompt.id,
                            variable_id=variable.id,
                            expected=variable.expected,
                            response=None,
                            grade=0,
                            time_elapsed=round(
                                time.perf_counter() - start_query_time, 2
                            ),
                            error=e.error,
                        )
                    )

                    counter += 1
                    print("Error:", e.error)

    print()
    print("SUMMARY")
    print()
    print("BY MODEL")
    calculate_results(outputs, MODELS)
    print()
    print("BY PROMPT")
    calculate_results(outputs, PROMPTS)
    print()
    print("BY VARIABLE")
    calculate_results(outputs, VARIABLES)
    print()
    print(f"Time taken: {time.perf_counter() - start_time:.0f} seconds")
    print(f"Saved results to: outputs/{run_id}")


if __name__ == "__main__":
    main()
