from utils.my_types import Prompt

prompts: list[Prompt] = [
    Prompt(
        id="v1",
        slots="{variable}",
        content="""Responda as seguintes perguntas sobre a seguinte certidão de julgamento. Responda em formato JSON. Caso a resposta envolva nomes, use apenas os primeiros nomes dos ministros. Caso não haja dados para necesários para responder, responda com `null`.
        
Perguntas:

1. qual foi o resultado do julgamento? responda com "ACEITO", "PARCIAL" ou "NEGADO"
2. a certidão menciona que o julgamento foi feito em sessão virtual? responda "SIM" ou "NAO"
3. a decisão foi tomada em unanimidade? responda com "SIM" OU "NAO"
4. houve efeitos modificativos? responda "SIM", "NAO" ou null
5. houve conhecer? responda com "SIM", "PARCIAL", "NAO" ou null
6. quais ministros votaram a favor?
7. quais ministros foram vencidos?
9. quais ministros fizeram voto-vista?
8. algum ministro lavrará o acórdão?


Exemplo de formato da resposta:
        
{
    "resultado": "ACEITO", 
    "online": "SIM",
    "unanimidade": "SIM",
    "modificativos": "NAO",
    "conhecer": "PARCIAL",
    "aFavor": "Benedito, Sérgio, Regina, Gurgel, Paulo",
    "vencidos": null,
    "votoVista": "Regina",
    "lavrara": null
    }


Aqui está o texto:
###
{variable}
###
""",
    ),
    Prompt(
        id="v2",
        slots="{{CERTIDAO}}",
        content="""Você foi encarregado de analisar um documento jurídico brasileiro chamado "certidão de julgamento" e responder a perguntas específicas sobre ele. Suas respostas devem ser fornecidas em formato JSON.

Aqui está o texto da certidão de julgamento:

<certidao>
{{CERTIDAO}}
</certidao>

Leia e analise cuidadosamente o texto acima para responder às seguintes perguntas:

1. Qual foi o resultado do julgamento? Responda com "ACEITO", "PARCIAL" ou "NEGADO".
2. A certidão menciona que o julgamento foi realizado em sessão virtual? Responda com "SIM" ou "NAO".
3. A decisão foi unânime (unanimidade)? Responda com "SIM" ou "NAO".
4. Houve efeitos modificativos? Responda com "SIM", "NAO" ou null.
5. Houve algum conhecimento (conhecer)? Responda com "SIM", "PARCIAL", "NAO" ou null.
6. Quais ministros votaram a favor?
7. Quais ministros foram vencidos?
8. Quais ministros fizeram um "voto-vista"?
9. Algum ministro vai lavrar o acórdão?

Instruções para responder:

1. Leia cuidadosamente todo o texto para reunir todas as informações relevantes.
2. Para perguntas que exigem respostas "SIM" ou "NAO", procure menções explícitas ou implicações claras no texto.
3. Para perguntas sobre ministros, use apenas os primeiros nomes em suas respostas.
4. Se não houver informações suficientes para responder a uma pergunta, use null como resposta.
5. Para a lista de ministros, separe os nomes com vírgulas se houver vários.
6. Certifique-se de que suas respostas reflitam com precisão as informações fornecidas no texto.

Forneça sua resposta no seguinte formato JSON:

<answer>
{
    "resultado": ,
    "online": ,
    "unanimidade": ,
    "modificativos": ,
    "conhecer": ,
    "aFavor": ,
    "vencidos": ,
    "votoVista": ,
    "lavrara": 
}
</answer>

Preencha os valores para cada chave com base em sua análise do texto. Lembre-se de usar null se não houver informações suficientes para responder a uma determinada pergunta.""",
    ),
]
