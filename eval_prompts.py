from my_types import Prompt

prompts: list[Prompt] = [
    Prompt(
        id="menciona",
        slots="{variable}",
        content="""Sua tarefa é analisar e responder se:
            a. o texto a seguir menciona a necessidade de comprar remédios ou itens de saúde; ou
            b. o texto menciona um evento imprevisto e excepcional que desorganizou a família; ou
            c. nenhum dos dois.
            Aqui está o texto:
            ###
            {variable}
            ###
            Primeiro, analise cuidadosamente o texto em um rascunho. Depois, responda "<<A >> (INDEFERIDO - SAÚDE)", "<<B>> (INDEFERIDO - EVENTO)" ou "<<C>> (DEFERIDO)".""",
    ),
    Prompt(
        id="deferimento",
        slots="{variable}",
        content="""Você irá analisar uma solicitação de benefício e determinar se ela  deve ser deferida ou indeferida com base nas regras fornecidas.
    Aqui estão as regras para determinar a elegibilidade:
    ###
    1. O benefício não pode ser deferido para a compra de remédios, insumos de saúde, órteses ou próteses.
    2. O benefício não pode ser deferido se não houver um fato novo e excepcional relatado no parecer.
    ###
    Aqui está a solicitação a ser analisada:
    ###
    {variable}
    ###
    Primeiro, analise cuidadosamente a solicitação e as regras em um <rascunho>. Considere se a solicitação menciona a necessidade de comprar remédios ou itens de saúde (o que levaria a um indeferimento pela regra 1) e se ela relata um evento imprevisto e excepcional que desorganizou a família (necessário para um deferimento pela regra 2).
    Depois de analisar, forneça sua resposta final em uma tag <resposta>. Responda:
    "A" se o parecer não contém um evento imprevisto que desorganizou a família
    "B" se o benefício não pode ser utilizado para adquirir medicamentos, insumos de saúde, órteses ou
    próteses
    "C" se o parecer contém um evento inesperado que desorganizou a família
    Inclua uma breve justificativa junto com a letra da resposta.""",
    ),
]
