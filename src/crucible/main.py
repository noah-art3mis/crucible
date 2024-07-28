from crucible.prompts import prompts_
from crucible.variables import variables_
from crucible.models import models_
from crucible.utils.grading import GradingType
from crucible.classes.Runner import Runner
from crucible.classes.Printer import Printer

from crucible.utils.io import load_models, load_prompts, load_variables

GRADING_TYPE = GradingType.EXACT  # qualitative uses gpt4o; use with care.
TEMPERATURE = 0.0
DANGER_MODE = True  # does not ask permission about prices; use with care.


def forge():

    MODELS = load_models(models_)
    PROMPTS = load_prompts(prompts_)
    VARIABLES = load_variables(variables_)

    runner = Runner(
        MODELS,
        PROMPTS,
        VARIABLES,
        GRADING_TYPE,
        DANGER_MODE,
        TEMPERATURE,
    )

    printer = Printer(runner)

    printer.display_start()
    runner.estimate_all_costs()

    printer.display_header()

    for task in runner.tasks:
        runner.run_task(task)
        printer.display_result(task)

    printer.display_report()
    printer.display_elapsed_time()


if __name__ == "__main__":
    forge()
