from utils.my_types import Model, Variable, Prompt
from utils.llm import query

GRADING_MODEL = Model("gpt-4o")
GRADING_PROMPT = """Rate this AI response from 0 to 10. Be brief.

This was the expected response:

{expected}

###

This was the AI response:

{response}

###

Be """


def grade_response(response: str, variable: Variable, grading_type: str) -> int | str:
    match grading_type:
        case "json":
            for expected in variable.expected:
                _response = response.replace("\n", "").replace(" ", "")
                _expected = expected.replace("\n", "").replace(" ", "")
                if _response in _expected:
                    return 1
            return 0

        case "binary":
            for expected in variable.expected:
                if response in expected:
                    return 1
            return 0

        case "qualitative":
            _model = GRADING_MODEL
            _variable = Variable(
                id="grading_variable", content=response, expected=[], options=[]
            )
            _prompt = Prompt(
                id="grading_prompt",
                slots="XXX",
                content=GRADING_PROMPT.replace(
                    "{expected}", variable.expected[0]
                ).replace("{response}", response),
            )
            response = query(
                model=_model,
                prompt=_prompt,
                variable=_variable,
                temp=0,
                danger_mode=True,
            )
            return response

        case _:
            raise ValueError(f"Unknown grading type: {grading_type}")
