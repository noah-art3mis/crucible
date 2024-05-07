from utils.my_types import Variable

options = ["<<A>>", "<<B>>", "<<C>>"]

variables: list[Variable] = [
    Variable(
        id="insegurança_alimentar",
        content="A família é composta pela mãe e os filhos Sofia (3) e Davi (5). Não possuem fonte de renda. Solicito o auxílio vulnerabilidade devido a situação de insegurança alimentar da família.",
        expected=["<<C>>"],
        options=options,
    ),
    Variable(
        id="fralda_geriátrica",
        content="Família residente em domicílio improvisado e tem um idoso acamado. Solicita-se o auxílio vulnerabilidade a fim de garantir a compra de fraldas geriátricas e outros insumos.",
        expected=["<<A>>"],
        options=options,
    ),
    Variable(
        id="acidente",
        content="Família monoparental composta por Maria e os filhos João (12) e Marcos (10). Tinham como fonte de renda o trabalho informal de Maria, mas esta sofreu um acidente e está impossibilidade de trabalhar. Solicita-se, portanto, o auxílio vulnerabilidade.",
        expected=["<<B>>"],
        options=options,
    ),
    Variable(
        id="remédios",
        content="A família está com o aluguel atrasado e necessita da compra de remédios para José (48), que tem lúpus. Solicita-se, portanto, o auxílio vulnerabilidade.",
        expected=["<<A>>"],
        options=options,
    ),
    Variable(
        id="pensão",
        content="Família composta por Jaqueline e a filha Helena (2). Tinham como fonte de renda a pensão alimentícia de Helena. No entanto, o progenitor deixou de realizar o pagamento há dois meses. Solicita-se, portanto, o auxílio vulnerabilidade, a fim de mitigar as desproteções vividas pela família.",
        expected=["<<B>>"],
        options=options,
    ),
    Variable(
        id="despesas_essenciais",
        content="Família monoparental composta por Josefa e 5 filhos com idades entre 1 e 17 anos. Contam apenas com a renda de coleta de material reciclável e relatam dificuldade para manter as despesas essenciais. Solicita-se, portanto, o auxílio vulnerabilidade.",
        expected=["<<C>>"],
        options=options,
    ),
]
