import sys
from dotenv import load_dotenv
import ollama
from openai import OpenAI
from utils.my_types import Model, Prompt, Variable
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

        if not danger_mode:
            estimate_costs(model.id, n_tokens)

            if not ask_permission():
                sys.exit(0)

        load_dotenv()
        client = OpenAI()
        response = client.chat.completions.create(
            model=model.id,
            messages=messages,  # type: ignore
            temperature=temp,
        )

        if not danger_mode:
            get_costs_gpt4o(response)

        return response.choices[0].message.content  # type: ignore

    raise ValueError("Invalid model type")


def build_messages(prompt: Prompt, variable: Variable) -> list[dict[str, str]]:
    if not variable:
        return [{"role": "user", "content": prompt.content}]

    # TODO
    text = prompt.content.replace(prompt.slot, variable.content)
    return [{"role": "user", "content": text}]
