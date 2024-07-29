from openai import OpenAI
import tiktoken
from dotenv import load_dotenv

from crucible.classes.Model import Model
from crucible.classes.Prompt import Prompt
from crucible.classes.Variable import Variable
from crucible.classes.Model import Source


class OpenAIModel(Model):
    def __init__(self, id: str) -> None:
        super().__init__(id)
        self.source = Source.OPENAI

    def _check_allowed_models(self, id: str) -> None:
        match id:
            case "gpt-4o":
                self.input = 5.0 / 1_000_000
                self.output = 15.0 / 1_000_000
                return
            case "gpt-4o-mini":
                self.input = 0.15 / 1_000_000
                self.output = 0.60 / 1_000_000
            case _:
                raise ValueError(f"Model {id} not found.")

    # override
    def estimate_costs(self, n_tokens: int) -> float:
        if n_tokens < 0:
            raise ValueError("n_tokens must be a positive integer.")

        input_cost = n_tokens * self.input
        output_cost = n_tokens * self.output
        total_cost = input_cost + output_cost
        return total_cost

    # override
    def get_n_tokens(self, text: str) -> int:
        encoding = tiktoken.encoding_for_model(self.id)
        tokenized = encoding.encode(text)
        n_tokens = len(tokenized)
        return n_tokens

    # override
    def calculate_cost(self, response: object) -> float:
        i_tokens = response.usage.prompt_tokens  # type: ignore
        o_tokens = response.usage.completion_tokens  # type: ignore

        input_cost = i_tokens * self.input
        output_cost = o_tokens * self.output
        total_cost = input_cost + output_cost

        print(f"\nActual Cost: {i_tokens} + {o_tokens} =  ${total_cost:.2f}")
        return total_cost

    # override
    def _get_completion(
        self, messages: list, temp: float, api_key: str | None
    ) -> object:
        if api_key is None:
            load_dotenv()

        client = OpenAI(api_key=api_key)
        return client.chat.completions.create(
            model=self.id,
            messages=messages,  # type: ignore
            temperature=temp,
        )

    # override
    def query(
        self,
        prompt: Prompt,
        variable: Variable,
        temp: float,
        api_key: str,
        danger_mode: bool,
    ):
        messages = self.build_messages(prompt, variable)
        response = self._get_completion(messages, temp, api_key)

        if not danger_mode:
            self.calculate_cost(response)

        return self._parse_completion(response)

    # override
    def _parse_completion(self, response: object) -> str:
        return response.choices[0].message.content  # type: ignore
