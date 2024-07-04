from utils.my_types import Variable

options = []

## ? !!! ESTÃO TODOS ERRADOS POIS NAO CONSTA O RELATOR NO TEXTO DA DECISAO !!!

## ??? terminar de fazer os comentados

variables: list[Variable] = [
    Variable(
        id="recurso negado",
        content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justiça, em sessão virtual de 03/10/2023 a 09/10/2023, por unanimidade, negar provimento ao recurso, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Benedito Gonçalves, Sérgio Kukina, Regina Helena Costa e Gurgel de Faria votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo Sérgio Domingues.",
        expected=[
            """```jsonl\n\n{"resultado": "NEGADO","unanimidade": "SIM","modificativos": "NAO","conhecer": null,"presidiu": "Paulo","ausente": null,"aFavor": "Benedito, Sérgio, Regina, Gurgel","vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
        ],
        options=options,
    ),
    # Variable(
    #     id="recurso parcial",
    #     content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justiça, em sessão virtual de 15/08/2023 a 21/08/2023, por unanimidade, dar parcial provimento ao recurso, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Sérgio Kukina, Regina Helena Costa, Gurgel de Faria e Paulo Sérgio Domingues votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo Sérgio Domingues.",
    #     expected=[
    #         """```jsonl\n\n{"resultado": null,"unanimidade": null,"modificativos": null,"conhecer": null,"presidiu": null,"ausente": null,"aFavor": null,"vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
    #     ],
    #     options=options,
    # ),
    # Variable(
    #     id="recurso aceito",
    #     content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justiça, em sessão virtual de 15/08/2023 a 21/08/2023, por unanimidade, dar provimento ao recurso, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Benedito Gonçalves, Sérgio Kukina, Regina Helena Costa e Paulo Sérgio Domingues votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo Sérgio Domingues.",
    #     expected=[
    #         """```jsonl\n\n{"resultado": null,"unanimidade": null,"modificativos": null,"conhecer": null,"presidiu": null,"ausente": null,"aFavor": null,"vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
    #     ],
    #     options=options,
    # ),
    # Variable(
    #     id="agravo negado",
    #     content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da Primeira Turma, por unanimidade, acolher os embargos declaração, com efeitos modificativos, para anular o acórdão de fls. 596/601 e, em novo julgamento, negar provimento ao agravo interno de fls. 578/588, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Sérgio Kukina, Regina Helena Costa e Gurgel de Faria votaram com o Sr. Ministro Relator. Ausente, justificadamente, o Sr. Ministro Benedito Gonçalves.",
    #     expected=[
    #         """```jsonl\n\n{"resultado": null,"unanimidade": null,"modificativos": null,"conhecer": null,"presidiu": null,"ausente": null,"aFavor": null,"vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
    #     ],
    #     options=options,
    # ),
    # Variable(
    #     id="agravo parcial",
    #     content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da Primeira Turma, por unanimidade, cancelar à afetação do feito à Primeira Seção e dar parcial provimento ao agravo regimental, apenas para tornar sem efeito a decisão de fls.135/141 e determinar o retorno dos autos à origem para nova apreciação do processo, considerando-se a tese vinculante fixada no Tema 1.007/STJ, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Benedito Gonçalves, Sérgio Kukina, Regina Helena Costa e Gurgel de Faria votaram com o Sr. Ministro Relator.",
    #     expected=[
    #         """```jsonl\n\n{"resultado": null,"unanimidade": null,"modificativos": null,"conhecer": null,"presidiu": null,"ausente": null,"aFavor": null,"vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
    #     ],
    #     options=options,
    # ),
    # Variable(
    #     id="agravo aceito",
    #     content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA, por unanimidade, dar provimento ao agravo interno, para arbitrar a verba honorária, com fundamento no art. 20, §§ 3º e 4º, do CPC/1973, no valor de R$ 60.000,00 (sessenta mil reais), nos termos do voto do Sr. Ministro Relator . Os Srs. Ministros Benedito Gonçalves, Sérgio Kukina e Gurgel de Faria votaram com o Sr. Ministro Relator. Impedida a Sra. Ministra Regina Helena Costa.",
    #     expected=[
    #         """```jsonl\n\n{"resultado": null,"unanimidade": null,"modificativos": null,"conhecer": null,"presidiu": null,"ausente": null,"aFavor": null,"vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
    #     ],
    #     options=options,
    # ),
    # Variable(
    #     id="embargo negado (rejeitado)",
    #     content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justiça, em sessão virtual de 07/11/2023 a 13/11/2023, por unanimidade, rejeitar os embargos de declaração, com aplicação de multa, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Benedito Gonçalves, Sérgio Kukina, Regina Helena Costa e Paulo Sérgio Domingues votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo Sérgio Domingues.",
    #     expected=[
    #         """```jsonl\n\n{"resultado": null,"unanimidade": null,"modificativos": null,"conhecer": null,"presidiu": null,"ausente": null,"aFavor": null,"vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
    #     ],
    #     options=options,
    # ),
    Variable(
        id="embargo parcial (acolhido parcialmente)",
        content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justiça, em sessão virtual de 21/11/2023 a 27/11/2023, por unanimidade, acolher parcialmente os embargos de declaração, sem efeitos modificativos, nos termos do voto da Sra. Ministra Relatora. Os Srs. Ministros Benedito Gonçalves, Sérgio Kukina, Gurgel de Faria e Paulo Sérgio Domingues votaram com a Sra. Ministra Relatora. Presidiu o julgamento o Sr. Ministro Paulo Sérgio Domingues.",
        expected=[
            """```jsonl\n\n{"resultado": "PARCIAL","unanimidade": "SIM","modificativos": "NAO","conhecer": null,"presidiu": "Paulo","ausente": null,"aFavor": "Benedito, Sérgio, Gurgel, Paulo, Regina","vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
        ],
        options=options,
    ),
    # Variable(
    #     id="embargo aceito (acolhido)",
    #     content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA, por unanimidade, acolher os embargos de declaração, com efeitos modificativos, para tornar sem efeito as decisões de fls. 173, 195/196 e 219/222, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Benedito Gonçalves, Regina Helena Costa, Gurgel de Faria e Paulo Sérgio Domingues votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo Sérgio Domingues.",
    #     expected=[
    #         """```jsonl\n\n{"resultado": null,"unanimidade": null,"modificativos": null,"conhecer": null,"presidiu": null,"ausente": null,"aFavor": null,"vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
    #     ],
    #     options=options,
    # ),
    Variable(
        id="maioria",
        content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da Primeira Turma do Superior Tribunal de Justiça, prosseguindo o julgamento, por maioria, vencido o Sr. Ministro Gurgel de Faria (Relator), dar parcial provimento ao agravo interno para reconhecer o interesse de agir, em razão da necessidade de prestação judicial para reconhecimento e cômputo de tempo especial negado administrativamente, fixando o termo inicial da aposentadoria especial na data da citação, nos termos do voto-vista da Sra. Ministra Regina Helena Costa, que lavrará acórdão. Votaram com a Sra. Ministra Regina Helena Costa os Srs. Ministros Paulo Sérgio Domingues (Presidente), Benedito Gonçalves e Sérgio Kukina.",
        expected=[
            """```jsonl\n\n{"resultado": "PARCIAL","unanimidade": "NAO","modificativos": null,"conhecer": null,"presidiu": "Sérgio","ausente": null,"aFavor": "Regina, Paulo, Benedito, Sérgio","vencidos": "Gurgel","lavrara": "Regina","desempate": null,"votoVista": "Regina"}\n\n```"""
        ],
        options=options,
    ),
    Variable(
        id="modificativos",
        content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justiça, em sessão virtual de 29/08/2023 a 04/09/2023, por unanimidade, acolher os embargos de declaração, com efeitos modificativos, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Sérgio Kukina, Regina Helena Costa, Gurgel de Faria e Paulo Sérgio Domingues votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo Sérgio Domingues.",
        expected=[
            """```jsonl\n\n{"resultado": "ACEITO","unanimidade": "SIM","modificativos": "SIM","conhecer": null,"presidiu": "Paulo","ausente": null,"aFavor": "Sérgio, Regina, Gurgel, Paulo","vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
        ],
        options=options,
    ),
    Variable(
        id="conhecer nan",
        content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da Primeira Turma, por unanimidade, dar provimento ao recurso especial, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Sérgio Kukina, Regina Helena Costa, Gurgel de Faria e Paulo Sérgio Domingues (Presidente) votaram com o Sr. Ministro Relator.",
        expected=[
            """```jsonl\n\n{"resultado": "ACEITO","unanimidade": "SIM","modificativos": null,"conhecer": null,"presidiu": "Sérgio","ausente": null,"aFavor": "Sérgio, Regina, Gurgel, Paulo","vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
        ],
        options=options,
    ),
    Variable(
        id="conhecer",
        content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da Primeira Turma, por unanimidade, conhecer do agravo para dar provimento ao recurso especial, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Sérgio Kukina, Regina Helena Costa, Gurgel de Faria e Paulo Sérgio Domingues (Presidente) votaram com o Sr. Ministro Relator.",
        expected=[
            """```jsonl\n\n{"resultado": "ACEITO","unanimidade": "SIM","modificativos": null,"conhecer": "SIM","presidiu": "Sérgio","ausente": null,"aFavor": "Sérgio, Regina, Gurgel, Paulo", "vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
        ],
        options=options,
    ),
    Variable(
        id="conhecer parcial",
        content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justiça, em sessão virtual de 26/09/2023 a 02/10/2023, por unanimidade, conhecer parcialmente do recurso, mas lhe negar provimento, nos termos do voto do Sr. Ministro Gurgel de Faria. Os Srs. Ministros Benedito Gonçalves, Sérgio Kukina, Regina Helena Costa e Paulo Sérgio Domingues votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo Sérgio Domingues.",
        expected=[
            """{"resultado": "NEGADO","unanimidade": "SIM","modificativos": "NAO","conhecer": "PARCIAL","presidiu": "Paulo","ausente": null,"aFavor": Benedito, Sérgio, Regina, Paulo","vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}"""
        ],
        options=options,
    ),
    Variable(
        id="nao conhecer",
        content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justiça, em sessão virtual de 21/11/2023 a 27/11/2023, por unanimidade, negar provimento ao agravo interno de fls. 28/33 e não conheçer do agravo interno de fls. 42/47, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Sérgio Kukina, Regina Helena Costa, Gurgel de Faria e Paulo Sérgio Domingues votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo Sérgio Domingues.",
        expected=[
            """```jsonl\n\n{"resultado": "NEGADO","unanimidade": "SIM","modificativos": null,"conhecer": "NAO","presidiu": "Paulo","ausente": null,"aFavor": "Sérgio, Regina, Gurgel, Paulo","vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
        ],
        options=options,
    ),
    Variable(
        id="ausente",
        content="Vistos, relatados e discutidos estes autos, acordam os Ministros da Primeira TURMA do Superior Tribunal de Justiça, por unanimidade, negar provimento ao agravo interno, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Regina Helena Costa, Gurgel de Faria(que ressalvou o seu ponto de vista) e Paulo Sérgio Domingues votaram com o Sr. Ministro Relator. Ausente, justificadamente, o Sr. Ministro Benedito Gonçalves.",
        expected=[
            """```jsonl\n\n{"resultado": "NEGADO","unanimidade": "SIM","modificativos": null,"conhecer": null,"presidiu": null,"ausente": "Benedito","aFavor": "Regina, Gurgel, Paulo", "vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
        ],
        options=options,
    ),
    Variable(
        id="lavrara",
        content="Visto e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da Primeira Turma do Superior Tribunal de Justiça, prosseguindo o julgamento, por maioria, vencidos os Srs. Ministros Benedito Gonçalves(Relator) e Gurgel de Faria(voto-vista), dar provimento ao recurso especial, a fim de reconhecer, in casu, a legitimidade ativa do Ministério Público Federal, nos termos do voto-vista da Sra. Ministra Regina Helena Costa, que lavrará o acórdão. Votaram com a Sra. Ministra Regina Helena Costa os Srs. Ministros Sérgio Kukina e Paulo Sérgio Domingues (Presidente).",
        expected=[
            """```jsonl\n\n{"resultado": "ACEITO","unanimidade": "NAO","modificativos": null,"conhecer": null,"presidiu": "Paulo","ausente": null,"aFavor": "Regina, Sérgio, Paulo","vencidos": "Benedito, Gurgel", "lavrara": "Regina","desempate": null,"votoVista": "Gurgel, Regina"}\n\n```"""
        ],
        options=options,
    ),
    Variable(
        id="desempate",
        content="Vistos, relatados e discutidos os autos em que são partes as acima indicadas, acordam os Ministros da Primeira Turma do Superior Tribunal de Justiça, prosseguindo o julgamento, após o voto-desempate do Sr. Ministro Benedito Gonçalves, por maioria, vencidos os Srs. Ministros Sérgio Kukina e Regina Helena Costa, negar provimento ao agravo interno do MPF, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Manoel Erhardt (Desembargador convocado do TRF-5ª Região) e Benedito Gonçalves (Presidente) votaram com o Sr. Ministro Relator.",
        expected=[
            """```jsonl\n\n{"resultado": "NEGADO","unanimidade": "NAO","modificativos": null,"conhecer": null,"presidiu": "Benedito","ausente": null,"aFavor": "Manoel, Benedito","vencidos": "Sérgio, Regina","lavrara": null,"desempate": "Benedito","votoVista": null}\n\n```"""
        ],
        options=options,
    ),
    Variable(
        id="voto vista 1",
        content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da Primeira Turma do Superior Tribunal de Justiça, prosseguindo o julgamento, por unanimidade, negar provimento ao agravo interno, nos termos do voto da Sra. Ministra Relatora. Os Srs. Ministros Gurgel de Faria (voto-vista), Manoel Erhardt (Desembargador convocado do TRF-5ª Região) e Sérgio Kukina (Presidente) votaram com a Sra. Ministra Relatora. Impedido o Sr. Ministro Benedito Gonçalves. Presidiu o julgamento o Sr. Ministro Sérgio Kukina.",
        expected=[
            """```jsonl\n\n{"resultado": "NEGADO","unanimidade": "SIM","modificativos": null,"conhecer": null,"presidiu": "Sérgio","ausente": "Benedito","aFavor": "Gurgel, Manoel, Sérgio","vencidos": null,"lavrara": null,"desempate": null,"votoVista": "Gurgel"}\n\n```"""
        ],
        options=options,
    ),
    Variable(
        id="voto vista 2",
        content="Vistos, relatados e discutidos estes autos, acordam os Ministros da Primeira TURMA do Superior Tribunal de Justiça, prosseguindo o julgamento, após o voto-vista do Sr. Ministro Benedito Gonçalves, por unanimidade, negar provimento ao agravo interno, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Regina Helena Costa, Gurgel de Faria, Paulo Sérgio Domingues (Presidente) e Benedito Gonçalves (voto-vista) votaram com o Sr. Ministro Relator.",
        expected=[
            """```jsonl\n\n{"resultado": "NEGADO","unanimidade": "SIM","modificativos": null,"conhecer": null,"presidiu": "Paulo","ausente": null,"aFavor": "Regina, Gurgel, Paulo, Benedito","vencidos": null,"lavrara": null,"desempate": null,"votoVista": "Benedito"}\n\n```"""
        ],
        options=options,
    ),
]
