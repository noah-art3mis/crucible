## Crucible

Lightweight prompt evaluation package.

Use online [here](https://crucible.streamlit.app/). Can also be used locally through streamlit. Can use [ollama](https://github.com/ollama/ollama-python) to run LLMs locally if necessary.

Cost estimation is very rough (input \* 2).

## Instructions

1.  Set the models, prompts and variables
1.  Set grading style and temperature
    -   `"EXACT"`: is either right or wrong. ignores line breaks and spaces in answer
    -   `"QUALITATIVE"`: ask gpt4o for feedback. be mindful of this token usage
1.  Click `compile`. Check the price estimation. Click `run`.
1.  Results are shown segmented by category.

## Parameters

-   `Model`

    -   id (str): name as understood by ollama. you might need to download it first
    -   source (str): "local" or "openai" or "anthropic"

    ```python
    Model("llama3", "local")
    ```

-   `Prompt`

    -   id (str): name of the test case
    -   slot (str): name of theslot which will be substituted by the variable in the prompt
    -   content (str): actual prompt

    ```python
    Prompt(
        id="test_3",
        slot="{variable}",
        content="""Sua tarefa é analisar e responder se o texto a seguir menciona a necessidade de comprar remédios ou itens de saúde. Aqui está o texto:\n\n###\n\n{variable}\n\n###\n\n\nPrimeiro, analise cuidadosamente o texto em um rascunho. Depois, responda: a solicitação citada menciona a necessidade de comprar remédios ou itens de saúde? Responda "<<SIM>>" ou "<<NÃO>>".""",
    )
    ```

-   `Variable`

    -   id (str): name of the test case
    -   content (str): text of snippet to be inserted in prompt
    -   expected (str list): values that would be considered correct
    -   options (str list): all values that the response could take. leave empty if does not apply

    ```python
    Variable(
        id="despesas_essenciais",
        content="Família monoparental composta por Josefa e 5 filhos com idades entre 1 e 17 anos. Contam apenas com a renda de coleta de material reciclável e relatam dificuldade para manter as despesas essenciais. Solicita-se, portanto, o auxílio vulnerabilidade.",
        expected=["<<NAO>>", "<<NÃO>>"],
    ),
    ```

## TODO

-   add tests
-   add instructions

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
