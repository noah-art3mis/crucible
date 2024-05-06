prompts = [
    {
        "id": "test_1",
        "content": """Sua tarefa é analisar e responder se:
        a. o texto a seguir menciona a necessidade de comprar remédios ou itens de saúde; ou 
        b. o texto menciona um evento imprevisto e excepcional que desorganizou a família; ou
        c. nenhum dos dois. 

        Aqui está o texto:

        ###
        {variable}
        ###

        Primeiro, analise cuidadosamente o texto em um rascunho. Depois, responda "<<A >> (INDEFERIDO - SAÚDE)", "<<B>> (INDEFERIDO - EVENTO)" ou "<<C>> (DEFERIDO)".""",
    }
]
