import re
from enum import Enum, auto

from utils.my_types import Model, Variable, Prompt
from utils.llm import query


class GradingType(Enum):
    EXACT = auto()
    QUALITATIVE = auto()


GRADING_MODEL = Model("gpt-4o", "openai")
GRADING_PROMPT = """Rate this AI response from 0 to 10. Give a be brief one line explanation for the rating.

This was the expected response:

{expected}

###

This was the AI response:

{response}

###"""

GRADING_PROMPT = """Sua tarefa é avaliar uma resposta de IA em uma escala de 0 a 10 e fornecer uma breve explicação para sua avaliação. Você receberá uma resposta esperada e a resposta real da IA para comparar.

Aqui está a resposta esperada:
<expected_response>
{expected}
</expected_response>

Aqui está a resposta da IA:
<ai_response>
{response}
</ai_response>

Compare a resposta da IA com a resposta esperada. Considere os seguintes fatores:
- Precisão das informações
- Integralidade da resposta
- Clareza e coerência
- Relevância para a pergunta
- Tom e estilo apropriados

Com base nesses fatores, avalie a resposta da IA em uma escala de 0 a 10, onde 0 é completamente incorreta ou irrelevante, e 10 é perfeita e indistinguível da resposta esperada.

Antes de fornecer sua avaliação, explique brevemente seu raciocínio em uma frase concisa. Considere os fatores mais importantes que influenciaram sua decisão.

Formate sua resposta da seguinte maneira:
<explanation>
[Sua explicação em uma frase aqui]
</explanation>
<rating>
[Sua avaliação numérica de 0 a 10 aqui]
</rating>

Certifique-se de que sua explicação seja clara e diretamente relacionada à avaliação que você fornece."""


def grade_response(
    response: str, variable: Variable, grading_type: GradingType
) -> tuple[int, str]:
    match grading_type:
        case GradingType.EXACT:
            for expected in variable.expected:
                _response = response.replace("\n", "").replace(" ", "")
                _expected = expected.replace("\n", "").replace(" ", "")
                if _response in _expected:
                    return 10, ""
            return 0, ""

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
            response = query(
                model=_model,
                prompt=_prompt,
                variable=_variable,
                temp=0,
                danger_mode=True,
            )
            return parse_grading(response)

        case _:
            raise ValueError(f"Unknown grading type: {grading_type}")


def parse_grading(grading: str) -> tuple[int, str]:

    grade_tags = r"<rating>(.*?)</rating>"
    info_tags = r"<explanation>(.*?)</explanation>"

    rating_match = re.search(grade_tags, grading, re.DOTALL)
    info_match = re.search(info_tags, grading, re.DOTALL)

    grade_text = rating_match.group(1).strip() if rating_match else "<<ERROR>>"
    info_text = info_match.group(1).strip() if info_match else "<<ERROR>>"

    return (int(grade_text), info_text)
