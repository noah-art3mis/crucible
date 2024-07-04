from openai import OpenAI
import sys
from utils.my_types import Model, Prompt, Variable
import ollama
from dotenv import load_dotenv
from utils.openai import (
    estimate_costs,
    get_n_tokens,
    get_costs_gpt4o,
    ask_permission,
)


def query(
    model: Model, prompt: Prompt, variable: Variable, temp: float, danger_mode: bool
) -> str:

    if model.id != "gpt-4o":
        response = ollama.chat(
            model=model.id,
            messages=build_messages(prompt, variable),  # type: ignore
            options={"temperature": temp},
        )
        return response["message"]["content"]  # type: ignore

    if model.id == "gpt-4o":

        messages = build_messages(prompt, variable)
        n_tokens = get_n_tokens(model.id, str(messages))
        estimate_costs(model.id, n_tokens)

        if not danger_mode:
            if not ask_permission():
                sys.exit(0)

        load_dotenv()
        client = OpenAI()
        response = client.chat.completions.create(
            model=model.id,
            messages=messages,  # type: ignore
            temperature=temp,
        )

        get_costs_gpt4o(response)

        return response.choices[0].message.content  # type: ignore

    raise ValueError("Invalid model type")


def build_messages(prompt: Prompt, variable: Variable) -> list[dict[str, str]]:
    if not variable:
        return [{"role": "user", "content": prompt.content}]

    text = prompt.content.replace("{variable}", variable.content)
    return [{"role": "user", "content": text}]
