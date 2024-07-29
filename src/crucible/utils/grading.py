import re
from enum import Enum, auto

from dotenv import load_dotenv

from crucible.classes.Prompt import Prompt
from crucible.classes.Variable import Variable
from crucible.utils.grading_config import GRADING_MODEL, GRADING_PROMPT


class GradingType(Enum):
    EXACT = auto()
    QUALITATIVE = auto()


def grade_response(
    response: str, variable: Variable, grading_type: GradingType, openai_api_key: str
) -> tuple[int, str]:

    match grading_type:

        case GradingType.EXACT:
            for expected in variable.expected:
                _response = response.replace("\n", "").replace(" ", "")
                _expected = expected.replace("\n", "").replace(" ", "")
                if _response in _expected:
                    return 10, "Exact match"
            return 0, "Not exact match"

        case GradingType.QUALITATIVE:

            _model = GRADING_MODEL

            _variable = Variable(
                id="grading_variable", content=response, expected=[], options=[]
            )

            _prompt = Prompt(
                id="grading_prompt",
                slot="{response}",
                content=GRADING_PROMPT.replace("{expected}", variable.expected[0]),
            )

            response = _model.query(
                prompt=_prompt,
                variable=_variable,
                temp=0,
                danger_mode=True,
                api_key=openai_api_key,
            )

            return _parse_quali_grading(response)

        case _:
            raise ValueError(f"Unknown grading type: {grading_type}")


def _parse_quali_grading(
    grading: str,
    rating: str = "rating",
    explanation: str = "explanation",
) -> tuple[int, str]:

    grade_tags = f"<{rating}>(.*?)</{rating}>"
    info_tags = f"<{explanation}>(.*?)</{explanation}>"

    rating_match = re.search(grade_tags, grading, re.DOTALL)
    info_match = re.search(info_tags, grading, re.DOTALL)

    grade_text = rating_match.group(1).strip() if rating_match else "<<ERROR>>"
    info_text = info_match.group(1).strip() if info_match else "<<ERROR>>"

    return (int(grade_text), info_text)
