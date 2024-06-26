## Crucible

Prompt evaluation package ("evals"). Test multiple models, prompts and variables.

Uses [ollama](https://github.com/ollama/ollama-python) to run LLMs locally.

## How to use

1. Setup: `python -m venv venv`, `source venv/bin/activate`, `pip install -r requirements.txt`
1. Set the models in `eval_models.py`, prompts in `eval_prompts.py` and variables in `eval_variables.py`. See section on parameters.
1. (Not implemented) Set grading style in `main.py`.
    - "binary": is either right or wrong
    - "qualitative": ask claude
1. Run `python eval.py`.
1. Logs from the run will be in `output/<datetime>.yaml`.

## Parameters

-   `model`

    -   id (str): name as understood by ollama. you might need to download it first

                  Model("llama3")

-   `prompt`

    -   id (str): name of the test case
    -   slots (str): name of snippet to be inserted in prompt
    -   content (str): actual prompt

                  Prompt(
                      id="test_3",
                      slots="{variable}",
                      content="""Sua tarefa é analisar e responder se o texto a seguir menciona a necessidade de comprar remédios ou itens de saúde. Aqui está o texto:\n\n###\n\n{variable}\n\n###\n\n\nPrimeiro, analise cuidadosamente o texto em um rascunho. Depois, responda: a solicitação citada menciona a necessidade de comprar remédios ou itens de saúde? Responda "<<SIM>>" ou "<<NÃO>>".""",
                  )

-   `variable`

    -   id (str): name of the test case
    -   content (str): text of snippet to be inserted in prompt
    -   expected (str list): values that would be considered correct
    -   options (str list): all values that the response could take

                  Variable(
                      id="despesas_essenciais",
                      content="Família monoparental composta por Josefa e 5 filhos com idades entre 1 e 17 anos. Contam apenas com a renda de coleta de material reciclável e relatam dificuldade para manter as despesas essenciais. Solicita-se, portanto, o auxílio vulnerabilidade.",
                      expected=["<<NAO>>", "<<NÃO>>"],
                      options=["<<NAO>>", "<<NÃO>>, <<SIM>>"],
                  ),

## TODO

-   add tests
-   add qualitative eval
-   add [asyncio](https://github.com/ollama/ollama-python?tab=readme-ov-file#async-client)
-   add details on which answers tend to be wrong. summary expected

## Resources

-   https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building_evals.ipynb
-   https://arize.com/blog-course/evaluating-prompt-playground/
-   https://www.confident-ai.com/blog/a-gentle-introduction-to-llm-evaluation
-   https://stephencollins.tech/posts/how-to-use-promptfoo-for-llm-testing
-   https://github.com/hegelai/prompttools
-   https://github.com/microsoft/promptbench
-   https://github.com/promptfoo/promptfoo
-   https://github.com/langfuse/langfuse
-   https://promptmetheus.com/
-   https://openshiro.com/
-   https://promptknit.com/
-   https://learnprompting.org/docs/tooling/IDEs/intro
-   https://www.promptotype.io/
-   https://langbear.runbear.io/introduction
