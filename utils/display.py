from utils.my_types import Model, Prompt, Result, Variable


def generate_and_show_summary(
    outputs: list[Result],
    category: list[Model] | list[Variable] | list[Prompt],
    grading_type: str,
):
    if grading_type == "binary" or grading_type == "json":
        max_grade_proportion = 1

    if grading_type == "qualitative":
        print("Grading type: qualitative. Read the logs.")
        return

    for item in category:
        subset = get_result_subset(item, outputs)
        max_grade = len(subset) * max_grade_proportion
        grade_absolute = sum(x.grade for x in subset if x.grade is not None)
        grade_relative = (grade_absolute / max_grade) * 100
        print("| ".join((item.id.ljust(30), f"Grade: {grade_relative:.0f}%")))


def get_result_subset(
    item: Model | Prompt | Variable, outputs: list[Result]
) -> list[Result]:
    if isinstance(item, Model):
        return [x for x in outputs if x.model == item.id]
    if isinstance(item, Prompt):
        return [x for x in outputs if x.prompt_id == item.id]
    if isinstance(item, Variable):
        return [x for x in outputs if x.variable_id == item.id]


def print_data(
    case, model, prompt, variable, case_id, grade, models, prompts, variables
):
    padding = 1
    max_widths = {
        case: len("99/99") + padding,
        model: max(len(str(x.id)) for x in models) + padding,
        prompt: max(len(str(x.id)) for x in prompts) + padding,
        variable: max(len(str(x.id)) for x in variables) + padding,
        case_id: 32 + padding,
        grade: len("grade") + padding,
    }
    header = "| ".join(name.ljust(max_widths[name]) for name in max_widths)
    print(header)
