from my_types import Model, Prompt, Result, Variable


def calculate_results(
    outputs: list[Result],
    category: list[Model] | list[Variable] | list[Prompt],
    grading_type="binary",
):
    if grading_type == "binary":
        max_grade_proportion = 1

    if grading_type == "out_of_ten":
        max_grade_proportion = 10

    if grading_type == "qualitative":
        raise NotImplementedError

    for item in category:
        subset = get_result_subset(item, outputs)
        max_grade = len(subset) * max_grade_proportion
        grade_absolute = sum(x.grade for x in subset)
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


def print_data(case, model, prompt, variable, grade, models, prompts, variables):
    padding = 1
    max_widths = {
        case: len("99/99") + padding,
        model: max(len(str(x.id)) for x in models) + padding,
        prompt: max(len(str(x.id)) for x in prompts) + padding,
        variable: max(len(str(x.id)) for x in variables) + padding,
        grade: len("grade") + padding,
    }
    header = "| ".join(name.ljust(max_widths[name]) for name in max_widths)
    print(header)
