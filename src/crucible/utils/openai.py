import tiktoken
from utils.my_types import Model

OMNI_INPUT = 5.0
OMNI_OUTPUT = 15.0

HAIKU_INPUT = 0.25
HAIKU_OUTPUT = 1.25

# @retry(tries=10, delay=1, backoff=2)
# def query_gpt(model: str, prompt: str, temp: float) -> str:
#     client = OpenAI()

#     message = client.chat.completions.create(
#         model=model,
#         temperature=temp,
#         messages=prompt,  # type: ignore
#     )
#     return message


# def get_prompt(prompt, snippet: str) -> str:
#     return prompt.replace("{snippet}", snippet)


# def get_messages(prompt: str):
#     messages = []
#     message = {"role": "user", "content": prompt}
#     messages.append(message)
#     return messages


def estimate_costs(model: Model, n_tokens: int) -> None:
    if model.id == "gpt-4o":
        MODEL_INPUT = OMNI_INPUT / 1_000_000
        MODEL_OUTPUT = OMNI_OUTPUT / 1_000_000
    elif model.id == "claude-3-haiku-20240307":
        MODEL_INPUT = HAIKU_INPUT / 1_000_000
        MODEL_OUTPUT = HAIKU_OUTPUT / 1_000_000
    else:
        raise ValueError("Model not supported: ", model)

    input_cost = n_tokens * MODEL_INPUT
    output_cost = n_tokens * MODEL_OUTPUT
    total_cost = input_cost + output_cost

    print(f"Estimated Cost: {n_tokens} + {n_tokens} =  ${total_cost:.2f}")


def get_actual_costs(model: Model, response: object) -> None:

    match model.id:
        case "gpt-4o":
            MODEL_INPUT = OMNI_INPUT / 1_000_000
            MODEL_OUTPUT = OMNI_OUTPUT / 1_000_000
            i_tokens = response.usage.prompt_tokens  # type: ignore
            o_tokens = response.usage.completion_tokens  # type: ignore
        case "claude-3-haiku-20240307":
            MODEL_INPUT = HAIKU_INPUT / 1_000_000
            MODEL_OUTPUT = HAIKU_OUTPUT / 1_000_000
            i_tokens = response.usage.input_tokens  # type: ignore
            o_tokens = response.usage.output_tokens  # type: ignore
        case _:
            raise ValueError("Model not supported: ", model)

    input_cost = i_tokens * MODEL_INPUT
    output_cost = o_tokens * MODEL_OUTPUT
    total_cost = input_cost + output_cost

    print(f"\nActual Cost: {i_tokens} + {o_tokens} =  ${total_cost:.2f}")


def get_n_tokens(model: Model, text: str) -> int:
    if model.source == "openai":
        encoding = tiktoken.encoding_for_model(model.id)
    else:
        encoding = tiktoken.get_encoding("cl100k_base")
    tokenized = encoding.encode(text)
    n_tokens = len(tokenized)
    return n_tokens


def ask_permission():
    while True:
        response = input("Are you sure you want to continue? (y/n): ").strip().lower()
        if response == "y":
            print("Permission granted. Continuing...")
            return True
        elif response == "n":
            print("Permission denied. Exiting...")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
