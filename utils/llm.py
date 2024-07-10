from typing import Iterable
from crucible.classes.Report import Model, Prompt, Variable
import ollama


def query(
    model: Model, prompt: Prompt, variable: Variable, temp: float
) -> Iterable[object]:
    response = ollama.chat(
        model=model.id,
        messages=build_messages(prompt, variable),  # type: ignore
        options={"temperature": temp},
    )
    return response


def build_messages(prompt: Prompt, variable: Variable) -> list[dict[str, str]]:
    if not variable:
        return [{"role": "user", "content": prompt.content}]

    text = prompt.content.replace("{variable}", variable.content)
    return [{"role": "user", "content": text}]
