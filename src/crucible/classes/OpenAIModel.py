from openai import OpenAI
import tiktoken
from dotenv import load_dotenv

from src.crucible.classes.Model import Model
from src.crucible.classes.Prompt import Prompt
from src.crucible.classes.Variable import Variable
from src.crucible.classes.Model import Source


class OpenAIModel(Model):
    def __init__(self, id: str) -> None:
        super().__init__(id)
        self.source = Source.OPENAI
        self.omni_input = 5.0 / 1_000_000
        self.omni_output = 15.0 / 1_000_000

    def _check_allowed_models(self, id: str) -> None:
        match id:
            case "gpt-4o":
                return
            case _:
                raise ValueError(f"Model {id} not found.")

    # override
    def estimate_costs(self, n_tokens: int) -> float:
        input_cost = n_tokens * self.omni_input
        output_cost = n_tokens * self.omni_output
        total_cost = input_cost + output_cost
        return total_cost

    # override
    def get_n_tokens(self, text: str) -> int:
        encoding = tiktoken.encoding_for_model(self.id)
        tokenized = encoding.encode(text)
        n_tokens = len(tokenized)
        return n_tokens

    # override
    def _get_actual_costs(self, response: object) -> None:
        i_tokens = response.usage.prompt_tokens  # type: ignore
        o_tokens = response.usage.completion_tokens  # type: ignore

        input_cost = i_tokens * self.omni_input
        output_cost = o_tokens * self.omni_output
        total_cost = input_cost + output_cost

        print(f"\nActual Cost: {i_tokens} + {o_tokens} =  ${total_cost:.2f}")

    # override
    def _get_completion(self, messages: list, temp: float) -> object:
        load_dotenv()
        client = OpenAI()
        return client.chat.completions.create(
            model=self.id,
            messages=messages,  # type: ignore
            temperature=temp,
        )

    # override
    def query(self, prompt: Prompt, variable: Variable, temp: float, danger_mode: bool):
        messages = self.build_messages(prompt, variable)
        response = self._get_completion(messages, temp)

        if not danger_mode:
            self._get_actual_costs(response)

        return self._parse_completion(response)

    # override
    def _parse_completion(self, response: object) -> str:
        return response.choices[0].message.content  # type: ignore
