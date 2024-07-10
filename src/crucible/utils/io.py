import yaml
from crucible.utils.my_types import Report, Model, Prompt, Variable


def save_logs(outputs: Report, run_id: str):
    with open(f"outputs/{run_id}.json", "w", encoding="utf-8") as f:
        yaml.dump(outputs.results, f, indent=2, allow_unicode=True, sort_keys=False)


def load_models(models: list[Model]):
    return models


def load_prompts(prompts: list[Prompt]):
    return prompts


def load_variables(variables: list[Variable]):
    return variables
