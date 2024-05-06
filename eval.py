import uuid
import time
import yaml
import ollama
import time
from eval_prompts import prompts
from eval_variables import variables, possible
from eval_models import models

MODELS = models
PROMPTS = prompts
VARIABLES = variables
POSSIBLE = possible
TEMPERATURE = 0.0


def main(run_id):
    start_time = time.perf_counter()
    print(f"Start eval")
    print(f"models: {MODELS}")
    print(f"prompts: {[x['id'] for x in PROMPTS]}")
    print(f"variables: {[x['id'] for x in VARIABLES]}")
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

    outputs = []

    counter = 0
    for model in MODELS:
        for prompt in PROMPTS:
            for variable in VARIABLES:
                try:
                    start_query_time = time.perf_counter()
                    output = query(model, prompt, variable)
                    response = output["message"]["content"]  # type: ignore
                    time_elapsed = f"{time.perf_counter() - start_query_time}:0.2f"
                    grade = grade_response(response, variable["expected"], POSSIBLE)
                    log = build_log(
                        model=model,
                        prompt=prompt,
                        variable=variable,
                        response=response,
                        grade=grade,
                        time_elapsed=time_elapsed,
                        error=None,
                    )

                    outputs.append(log)

                    counter += 1
                    print(
                        f"{counter}/{total_cases:<3} | {model:<6} | {prompt['id']:<10} | {variable['id']:<30} | {grade}/10"
                    )

                    with open(f"outputs/{run_id}.yaml", "w", encoding="utf-8") as f:
                        yaml.dump(
                            outputs, f, indent=2, allow_unicode=True, sort_keys=False
                        )

                except ollama.ResponseError as e:
                    time_elapsed = f"{time.perf_counter() - start_query_time:0.2f}"
                    log = build_log(
                        model=model,
                        prompt=prompt,
                        variable=variable,
                        response=None,
                        grade=None,
                        time_elapsed=time_elapsed,
                        error=e.error,
                    )
                    counter += 1
                    outputs.append(log)
                    print("Error:", e.error)

    print_results(outputs)

    print(f"Time taken: {time.perf_counter() - start_time:.2f} seconds")


def query(model, prompt, variable):
    response = ollama.chat(
        model=model,
        messages=build_prompt(prompt, variable),  # type: ignore
        options={"temperature": TEMPERATURE},
    )
    return response


def build_prompt(prompt_template, variable):
    text = prompt_template["content"].replace("{variable}", variable["content"])
    if not text:
        raise Exception

    messages = [{"role": "user", "content": text}]
    return messages


def grade_response(response, expected, possible_responses=None):
    grade = 0  # out of 10

    if expected in response:
        grade = 10

    if possible_responses:
        other_responses = set(possible_responses) - {expected}
        for other in other_responses:
            if other in response:
                grade -= 5

    return max(grade, 0)


def build_log(
    model,
    prompt,
    variable,
    response,
    grade,
    time_elapsed,
    error,
):
    return {
        "id": uuid.uuid4().hex,
        "model": model,
        "prompt_id": prompt["id"],
        "variable_id": variable["id"],
        "expected": variable["expected"],
        "grade": grade,
        "time_elapsed": time_elapsed,
        "error": error,
        "output": response,
    }


def print_results(outputs):
    print("---")
    calculate_results(outputs, MODELS, "model")
    for model in MODELS:
        model_results = [x for x in outputs if x["model"] == model]
        max_grade = len(model_results) * 10
        model_grade_absolute = sum([x["grade"] for x in model_results])
        model_grade_relative = model_grade_absolute / max_grade
        print(f"Model: {model:<5} | Grade: {model_grade_relative:.0f}%")

    for prompt in PROMPTS:
        prompt_results = [x for x in model_results if x["prompt_id"] == prompt["id"]]
        prompt_grade = (
            sum([x["grade"] for x in prompt_results]) / len(prompt_results) * 10
        )
        print(f"Prompt: {prompt['id']:<10} | Grade: {prompt_grade:.1f}")

    for variable in VARIABLES:
        variable_results = [x for x in outputs if x["variable_id"] == variable["id"]]
        variable_grade = (
            sum([x["grade"] for x in variable_results]) / len(variable_results) * 10
        )
        print(f"Variable: {variable['id']:<10} | Grade: {variable_grade:.1f}")

    print("---")


def calculate_results(outputs, category, column_id, max_grade=10):

    for item in category:
        category_results = [x for x in outputs if x[column_id] == item]
        category_max_grade = len(model_results) * max_grade
        model_grade_absolute = sum([x["grade"] for x in category_results])
        model_grade_relative = model_grade_absolute / category_max_grade
        print(f"{category}: {item:<5} | Grade: {model_grade_relative:.0f}%")


if __name__ == "__main__":
    run_id = time.strftime("%Y%m%d%H%M%S")
    main(run_id)
    print(f"Saved results to: outputs/{run_id}")
