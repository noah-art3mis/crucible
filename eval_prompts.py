from utils.my_types import Prompt

prompts: list[Prompt] = [
    Prompt(
        id="stj1",
        slots="{variable}",
        content="""Responda as seguintes perguntas sobre o texto a seguir. Responda em formato JSONL. Caso a resposta envolva nomes, use apenas os primeiros nomes dos ministros. Caso não haja dados para necesários para responder, responda com "null".
        
Perguntas:

1. qual foi o resultado da decisão tomada? responda com "ACEITO", "PARCIAL" ou "NEGADO"
2. a decisão foi tomada em unanimidade? responda com "SIM" OU "NAO"
3. houve efeitos modificativos? responda "SIM" ou "NAO"
4. houve conhecer? responda com "SIM", "PARCIAL" ou "NAO"
5. qual ministro presidiu o julgamento?
6. houve algum ministro ausente?
7. quais ministros votaram a favor?
8. algum ministro foi vencido?
9. algum ministro lavrará o acórdão?
10. de quem foi o voto de desempate?
11. quais ministros fizeram voto-vista?


Exemplo de formato da resposta:
        
{"resultado": "ACEITO","unanimidade": "SIM","modificativos": "NAO","conhecer": "PARCIAL","presidiu": "Paulo","ausente": null,"aFavor": "Benedito, Sérgio, Regina, Gurgel","vencidos": null,"lavrara": null,"desempate": null,"votoVista": "Regina"}


Aqui está o texto:
###
{variable}
###
""",
    ),
]


# @dataclass
# class Decisao:
#     id: str
#     decisao: str
#     unanimidade: bool
#     modificativos: bool
#     resultado: str  # "aceito" | "parcial" | "negado"
#     conhecer: Optional[str]  # "sim" | "parcial" | "nao" | NaN
#     aFavor: Optional[str]  # ministros
#     vencidos: Optional[str]  # ministros
#     presidiu: Optional[str]  # ministros
#     ausente: Optional[str]  # ministros
#     lavrara: Optional[str]  # ministros
#     desempate: Optional[str]  # ministros
#     votoVista: Optional[str]  # ministros
