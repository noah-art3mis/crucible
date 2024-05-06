from typing import Iterable
import uuid
import time
import yaml
import ollama
import time
from eval_prompts import prompts
from eval_variables import variables
from eval_models import models
from my_types import Result, Prompt, Variable, Model

MODELS = models
PROMPTS = prompts
VARIABLES = variables
TEMPERATURE = 0.0


def main(run_id):
    start_time = time.perf_counter()
    print(f"Start eval")
    print(f"models: {[x.id for x in MODELS]}")
    print(f"prompts: {[x.id for x in PROMPTS]}")
    print(f"variables: {[x.id for x in VARIABLES]}")
    total_cases = len(MODELS) * len(PROMPTS) * len(VARIABLES)
    print(f"total cases: {total_cases}")

    if len(MODELS) == 0:
        print("No models provided")
        return
    if len(PROMPTS) == 0:
        print("No prompts provided")
        return
    if len(VARIABLES) == 0:
        print("No variables provided")
        return

    outputs: list[Result] = []

    print(
        f"{'case':<6} | {'model':<6} | {'prompt':<10} | {'variable':<30} | {'grade':<10} | {'status'}"
    )

    counter = 0
    for model in MODELS:
        for prompt in PROMPTS:
            for variable in VARIABLES:
                try:
                    start_query_time = time.perf_counter()
                    output = query(model, prompt, variable, TEMPERATURE)
                    response = output["message"]["content"]  # type: ignore
                    grade = grade_response(response, variable)

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
                    print(
                        f"{counter}/{total_cases:<6} | {model.id:<6} | {prompt.id:<10} | {variable.id:<30} | {str(grade) + '/10':<10} | {'ok' if grade == 10 else 'FAIL'}"
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

    # print("---")
    # calculate_results(outputs, MODELS)
    # print("---")
    # calculate_results(outputs, PROMPTS)
    # print("---")
    # calculate_results(outputs, VARIABLES)
    # print("---")

    print(f"Time taken: {time.perf_counter() - start_time:.2f} seconds")


def query(
    model: Model, prompt: Prompt, variable: Variable, temp: float
) -> Iterable[object]:
    response = ollama.chat(
        model=model.id,
        messages=build_messages(prompt, variable),  # type: ignore
        options={"temperature": temp},
    )
    return response


def build_messages(prompt: Prompt, variable: Variable) -> list[dict[str, str]]:
    text = prompt.content.replace("{variable}", variable.content)
    if not text:
        raise Exception

    messages = [{"role": "user", "content": text}]
    return messages


def grade_response(response: str, variable: Variable) -> int:
    grade = 0  # out of 10

    expected = variable.expected
    possible_responses = variable.options

    if expected in response:
        grade = 10

    # penalize if it cites other possible responses
    if possible_responses:
        other_responses = set(possible_responses) - {expected}
        for other in other_responses:
            if other in response:
                grade -= 5

    return int(max(grade, 0))


def calculate_results(outputs: list[Result], category: list, max_grade=10):
    for item in category:
        subset = get_result_subset(item, outputs)
        max_grade = len(subset) * max_grade
        grade_absolute = sum(x.grade for x in subset)
        grade_relative = (grade_absolute / max_grade) * 100
        print(f"{item.id:<30}| Grade: {grade_relative:.0f}%")


# THIS IS STILL BROKEN
def get_result_subset(
    item: Model | Prompt | Variable, outputs: list[Result]
) -> list[Result]:
    if isinstance(item, Model):
        return [x for x in outputs if x.model == item.id]
    if isinstance(item, Prompt):
        return [x for x in outputs if x.prompt_id == item.id]
    if isinstance(item, Variable):
        return [x for x in outputs if x.variable_id == item.id]


if __name__ == "__main__":
    run_id = time.strftime("%Y%m%d%H%M%S")
    main(run_id)
    print(f"Saved results to: outputs/{run_id}")
