from crucible.classes.Variable import Variable

variables_: list[Variable] = [
    Variable(
        id="sessao presencial",
        content="Processo: 366017 | Ministro Relator: PAULO S\u00c9RGIO DOMINGUES | Certid\u00e3o de Julgamento: Vistos e relatados estes autos em que s\u00e3o partes as acima indicadas, acordam os Ministros da Primeira Turma, por unanimidade, negar provimento ao agravo interno, em ju\u00edzo de retrata\u00e7\u00e3o, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Benedito Gon\u00e7alves, S\u00e9rgio Kukina, Regina Helena Costa e Gurgel de Faria votaram com o Sr. Ministro Relator.",
        expected=[
            """```json

{
"resultado": "NEGADO",
"online": "NAO",
"unanimidade": "SIM",
"modificativos": null,
"conhecer": null,
"aFavor": "Benedito, Gurgel, Paulo, Regina, Sérgio",
"vencidos": null,
"votoVista": null,
"lavrara": null
}

```"""
        ],
    ),
    # Variable(
    #     id="recurso negado",
    #     content="Processo: 2089458 | Ministro Relator: GURGEL DE FARIA | Certid\u00e3o de Julgamento: Vistos e relatados estes autos em que s\u00e3o partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justi\u00e7a, em sess\u00e3o virtual de 26/09/2023 a 02/10/2023, por unanimidade, negar provimento ao recurso, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Benedito Gon\u00e7alves, S\u00e9rgio Kukina, Regina Helena Costa e Paulo S\u00e9rgio Domingues votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo S\u00e9rgio Domingues.",
    #     expected=[
    #         """```json
    # {
    # "resultado": "NEGADO",
    # "online": "SIM",
    # "unanimidade": "SIM",
    # "modificativos": null,
    # "conhecer": null,
    # "aFavor": "Benedito, Gurgel, Paulo, Regina, Sérgio",
    # "vencidos": null,
    # "votoVista": null,
    # "lavrara": null
    # }
    # ```"""
    #     ],
    # ),
    #     # Variable(id="recurso parcial", content="", expected=[], options=options),
    #     # Variable(id="recurso aceito", content="", expected=[], options=options),
    #     # Variable(id="agravo negado", content="", expected=[], options=options),
    #     # Variable(id="agravo parcial", content="", expected=[], options=options),
    #     Variable(
    #         id="agravo aceito",
    #         content="Processo: 2380545 | Ministro Relator: GURGEL DE FARIA | Certid\u00e3o de Julgamento: Vistos e relatados estes autos em que s\u00e3o partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA, por unanimidade, dar provimento ao agravo interno de TERRACOM CONSTRU\u00c7\u00d5ES LTDA., com aplica\u00e7\u00e3o de efeito expansivo ao litisconsorte passivo, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Benedito Gon\u00e7alves, S\u00e9rgio Kukina, Regina Helena Costa e Paulo S\u00e9rgio Domingues votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo S\u00e9rgio Domingues.",
    #         expected=[
    #             """```json
    # {
    # "resultado": "ACEITO",
    # "online": "NAO",
    # "unanimidade": "SIM",
    # "modificativos": null,
    # "conhecer": null,
    # "aFavor": "Benedito, Gurgel, Paulo, Regina, Sérgio",
    # "vencidos": null,
    # "votoVista": null,
    # "lavrara": null
    # }
    # ```"""
    #         ],
    #
    #     ),
    #     # Variable(id="embargo negado (rejeitado)", content="", expected=[], options=options),
    #     Variable(
    #         id="embargo parcial",
    #         content="Processo: 70331 | Ministro Relator: REGINA HELENA COSTA | Certid\u00e3o de Julgamento: Vistos e relatados estes autos em que s\u00e3o partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justi\u00e7a, em sess\u00e3o virtual de 12/09/2023 a 18/09/2023, por unanimidade, acolher parcialmente os embargos de declara\u00e7\u00e3o, com efeitos modificativos, nos termos do voto da Sra. Ministra Relatora. Os Srs. Ministros Benedito Gon\u00e7alves, S\u00e9rgio Kukina, Gurgel de Faria e Paulo S\u00e9rgio Domingues votaram com a Sra. Ministra Relatora. Presidiu o julgamento o Sr. Ministro Paulo S\u00e9rgio Domingues.",
    #         expected=[
    #             """```json
    # {
    # "resultado": "PARCIAL",
    # "online": "SIM",
    # "unanimidade": "SIM",
    # "modificativos": "SIM",
    # "conhecer": null,
    # "aFavor": "Benedito, Gurgel, Paulo, Regina, Sérgio",
    # "vencidos": null,
    # "votoVista": null,
    # "lavrara": null
    # }
    # ```"""
    #         ],
    #
    #     ),
    #     # Variable(id="embargo aceito (acolhido)", content="", expected=[], options=options),
    #     Variable(
    #         id="maioria",
    #         content="Processo: 1870577 | Ministro Relator: GURGEL DE FARIA | Certid\u00e3o de Julgamento: Prosseguindo o julgamento, a Primeira Turma, por maioria, vencido o Sr. Ministro S\u00e9rgio Kukina(Relator), deu provimento ao agravo interno, para negar provimento ao recurso especial, nos termos do voto-vista do Sr. Ministro Gurgel de Faria, que lavrar\u00e1 o ac\u00f3rd\u00e3o. Votaram com o Sr. Ministro Gurgel de Faria os Srs. Ministros Regina Helena Costa e Paulo S\u00e9rgio Domingues (Presidente).N\u00e3o participou do julgamento o Sr. Ministro Benedito Gon\u00e7alves.",
    #         expected=[
    #             """```json
    # {
    # "resultado": "NEGADO",
    # "online": "NAO",
    # "unanimidade": "NAO",
    # "modificativos": null,
    # "conhecer": null,
    # "aFavor": "Gurgel, Paulo, Regina",
    # "vencidos": "Sérgio",
    # "votoVista": "Gurgel",
    # "lavrara": "Gurgel"
    # }
    # ```"""
    #         ],
    #
    #     ),
    #     # Variable(id="modificativos sim", content="", expected=[], options=options),
    #     Variable(
    #         id="modificativos nao",
    #         content="Processo: 2062961 | Ministro Relator: S\u00c9RGIO KUKINA | Certid\u00e3o de Julgamento: Vistos e relatados estes autos em que s\u00e3o partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justi\u00e7a, em sess\u00e3o virtual de 24/10/2023 a 30/10/2023, por unanimidade, acolher parcialmente os embargos de declara\u00e7\u00e3o, sem efeitos modificativos, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Benedito Gon\u00e7alves, Regina Helena Costa, Gurgel de Faria e Paulo S\u00e9rgio Domingues votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo S\u00e9rgio Domingues.",
    #         expected=[
    #             """```json
    # {
    # "resultado": "PARCIAL",
    # "online": "SIM",
    # "unanimidade": "SIM",
    # "modificativos": "NAO",
    # "conhecer": null,
    # "aFavor": "Benedito, Gurgel, Paulo, Regina, Sérgio",
    # "vencidos": null,
    # "votoVista": null,
    # "lavrara": null
    # }
    # ```"""
    #         ],
    #
    #     ),
    #     # Variable(id="modificativos null", content="", expected=[], options=options),
    #     Variable(
    #         id="conhecer sim",
    #         content="Processo: 1340335 | Ministro Relator: BENEDITO GON\u00c7ALVES | Certid\u00e3o de Julgamento: Vistos e relatados estes autos em que s\u00e3o partes as acima indicadas, acordam os Ministros da Primeira Turma, por unanimidade, conhecer do recurso especial e dar-lhe provimento com determina\u00e7\u00e3o de devolu\u00e7\u00e3o dos autos ao Tribunal Regional Federal da 5\u00aa Regi\u00e3o, a fim de que aquela Corte arbitre o valor da indeniza\u00e7\u00e3o como entender de direito, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros S\u00e9rgio Kukina, Regina Helena Costa, Gurgel de Faria e Paulo S\u00e9rgio Domingues votaram com o Sr. Ministro Relator.",
    #         expected=[
    #             """```json
    # {
    # "resultado": "ACEITO",
    # "online": "NAO",
    # "unanimidade": "SIM",
    # "modificativos": null,
    # "conhecer": "SIM",
    # "aFavor": "Benedito, Gurgel, Paulo, Regina, Sérgio",
    # "vencidos": null,
    # "votoVista": null,
    # "lavrara": null
    # }
    # ```"""
    #         ],
    #
    #     ),
    #     Variable(
    #         id="conhecer parcial",
    #         content="Processo: 2006155 | Ministro Relator: S\u00c9RGIO KUKINA | Certid\u00e3o de Julgamento: Vistos e relatados estes autos em que s\u00e3o partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justi\u00e7a, em sess\u00e3o virtual de 23/05/2023 a 29/05/2023, por unanimidade, conhecer parcialmente do recurso, mas lhe negar provimento, nos termos do voto do Sr. Ministro S\u00e9rgio Kukina. Os Srs. Ministros Benedito Gon\u00e7alves, Regina Helena Costa, Gurgel de Faria e Paulo S\u00e9rgio Domingues votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo S\u00e9rgio Domingues.",
    #         expected=[
    #             """```json
    # {
    # "resultado": "NEGADO",
    # "online": "SIM",
    # "unanimidade": "SIM",
    # "modificativos": null,
    # "conhecer": "PARCIAL",
    # "aFavor": "Benedito, Gurgel, Paulo, Regina, Sérgio",
    # "vencidos": null,
    # "votoVista": null,
    # "lavrara": null
    # }
    # ```"""
    #         ],
    #
    #     ),
    #     Variable(
    #         id="conhecer nao",
    #         content="Processo: 1845055 | Ministro Relator: S\u00c9RGIO KUKINA | Certid\u00e3o de Julgamento: Vistos e relatados estes autos em que s\u00e3o partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justi\u00e7a, em sess\u00e3o virtual de 05/03/2024 a 11/03/2024, por unanimidade, n\u00e3o conhecer do recurso, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Benedito Gon\u00e7alves, Regina Helena Costa, Gurgel de Faria e Paulo S\u00e9rgio Domingues votaram com o Sr. Ministro Relator. Presidiu o julgamento o Sr. Ministro Paulo S\u00e9rgio Domingues.",
    #         expected=[
    #             """```json
    # {
    # "resultado": "NEGADO",
    # "online": "SIM",
    # "unanimidade": "SIM",
    # "modificativos": null,
    # "conhecer": "NAO",
    # "aFavor": "Benedito, Gurgel, Paulo, Regina, Sérgio",
    # "vencidos": null,
    # "votoVista": null,
    # "lavrara": null
    # }
    # """
    #         ],
    #
    #     ),
    #     # Variable(id="conhecer null", content="", expected=[], options=options),
    #     # Variable(id="nao conhecer", content="", expected=[], options=options),
    #     # Variable(id="lavrara", content="", expected=[], options=options),
    #     Variable(
    #         id="voto vista",
    #         content="Processo: 1723732 | Ministro Relator: PAULO S\u00c9RGIO DOMINGUES | Certid\u00e3o de Julgamento: Vistos e relatados estes autos em que s\u00e3o partes as acima indicadas, acordam os Ministros da PRIMEIRA TURMA do Superior Tribunal de Justi\u00e7a, prosseguindo o julgamento, ap\u00f3s o voto-vista do Sr. Ministro Benedito Gon\u00e7alves, por unanimidade, negar provimento ao agravo interno, nos termos do voto do Sr. Ministro Relator. Os Srs. Ministros Benedito Gon\u00e7alves (voto-vista), S\u00e9rgio Kukina, Regina Helena Costa e Gurgel de Faria votaram com o Sr. Ministro Relator.",
    #         expected=[
    #             """```json
    # {
    # "resultado": "NEGADO",
    # "online": "NAO",
    # "unanimidade": "SIM",
    # "modificativos": null,
    # "conhecer": null,
    # "aFavor": "Benedito, Gurgel, Paulo, Regina, Sérgio",
    # "vencidos": null,
    # "votoVista": "Benedito",
    # "lavrara": null
    # }
    # ```"""
    #         ],
    #
    #     ),
]
