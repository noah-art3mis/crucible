from utils.my_types import Variable

options = []

variables: list[Variable] = [
    Variable(
        id="recurso negado",
        content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justiça, em sessão virtual de 03/10/2023 a 09/10/2023, por unanimidade, negar provimento ao recurso, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Benedito Gonçalves, Sérgio Kukina, Regina Helena Costa e Gurgel de Faria votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo Sérgio Domingues.",
        expected=[
            """```jsonl\n\n{"resultado": "NEGADO","unanimidade": "SIM","modificativos": "NAO","conhecer": null,"presidiu": "Paulo","ausente": null,"aFavor": "Benedito, Sérgio, Regina, Gurgel","vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}\n\n```"""
        ],
        options=options,
    ),
    # Variable(id="recurso parcial"),
    # Variable(id="recurso aceito"),
    # Variable(id="agravo negado"),
    # Variable(id="agravo parcial"),
    # Variable(id="agravo aceito"),
    # Variable(id="x negado"),
    # Variable(id="x parcial"),
    # Variable(id="x aceito"),
    # Variable(id="maioria"),
    # Variable(id="modificativos"),
    # Variable(id="conhecer nan"),
    # Variable(id="conhecer"),
    # Variable(
    #     id="conhecer parcial",
    #     content="Vistos e relatados estes autos em que são partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justiça, em sessão virtual de 26/09/2023 a 02/10/2023, por unanimidade, conhecer parcialmente do recurso, mas lhe negar provimento, nos termos do voto do Sr. Ministro Gurgel de Faria. Os Srs. Ministros Benedito Gonçalves, Sérgio Kukina, Regina Helena Costa e Paulo Sérgio Domingues votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo Sérgio Domingues.",
    #     expected=[
    #         """{"resultado": "NEGADO","unanimidade": "SIM","modificativos": "NAO","conhecer": "PARCIAL","presidiu": "Paulo","ausente": null,"aFavor": Benedito, Sérgio, Regina, Paulo","vencidos": null,"lavrara": null,"desempate": null,"votoVista": null}"""
    #     ],
    #     options=options,
    # ),
    # Variable(id="nao conhecer"),
    # Variable(id="ausente"),
    # Variable(id="lavrara"),
    # Variable(id="desempate"),
    # Variable(id="voto vista 1"),
    # Variable(id="voto vista 2"),
]
