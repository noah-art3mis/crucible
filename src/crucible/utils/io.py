from crucible.classes.Model import Model
from crucible.classes.Prompt import Prompt
from crucible.classes.Variable import Variable


# def save_report(self, run_id: str) -> None:
#     with open(f"outputs/{run_id}.yaml", "w", encoding="utf-8") as f:
#         yaml.dump(self.report.results, f, indent=2, allow_unicode=True, sort_keys=False)


def load_models(models: list[Model]):
    return models


def load_prompts(prompts: list[Prompt]):
    return prompts


def load_variables(variables: list[Variable]):
    return variables
