from crucible.classes.OpenAIModel import OpenAIModel


GRADING_MODEL = OpenAIModel("gpt-4o")

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
