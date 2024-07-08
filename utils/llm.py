import re
import sys
from dotenv import load_dotenv
import ollama
import anthropic
from openai import OpenAI
from utils.my_types import Model, Prompt, Variable
from utils.openai import (
    estimate_costs,
    get_n_tokens,
    get_actual_costs,
    ask_permission,
)


def query(
    model: Model, prompt: Prompt, variable: Variable, temp: float, danger_mode: bool
) -> str:

    if model.source == "local":
        response = ollama.chat(
            model=model.id,
            messages=build_messages(prompt, variable),  # type: ignore
            options={"temperature": temp},
        )
        return response["message"]["content"]  # type: ignore

    if model.source == "openai":

        messages = build_messages(prompt, variable)
        n_tokens = get_n_tokens(model, str(messages))

        if not danger_mode:
            estimate_costs(model, n_tokens)

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
            get_actual_costs(model, response)

        return response.choices[0].message.content  # type: ignore

    if model.source == "anthropic":
        messages = build_messages(prompt, variable)
        n_tokens = get_n_tokens(model, str(messages))

        if not danger_mode:
            estimate_costs(model, n_tokens)

            if not ask_permission():
                sys.exit(0)

        load_dotenv()
        client = anthropic.Anthropic()
        response = client.messages.create(
            model=model.id,
            max_tokens=4096,
            temperature=0,
            messages=messages,  # type: ignore
        )

        if not danger_mode:
            get_actual_costs(model, response)

        return parse_completion(response.content[0].text)  # type: ignore

    raise ValueError("Invalid model: ", model)


def build_messages(prompt: Prompt, variable: Variable) -> list[dict[str, str]]:
    if not variable:
        return [{"role": "user", "content": prompt.content}]

    # TODO
    text = prompt.content.replace(prompt.slot, variable.content)
    return [{"role": "user", "content": text}]


def parse_completion(completion) -> str:
    answer_pattern = r"<answer>(.*?)</answer>"
    answer_match = re.search(answer_pattern, completion, re.DOTALL)
    answer_text = answer_match.group(1).strip() if answer_match else completion
    return answer_text
