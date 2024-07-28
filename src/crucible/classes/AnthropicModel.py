import anthropic
from dotenv import load_dotenv

from crucible.classes.Model import Model
from crucible.classes.Prompt import Prompt
from crucible.classes.Variable import Variable
from crucible.classes.Model import Source


class AnthropicModel(Model):
    def __init__(self, id: str):
        super().__init__(id)
        self.source = Source.ANTHROPIC

    # override
    def _check_allowed_models(self, id: str) -> None:
        match id:
            case "claude-3-haiku-20240307":
                self.input = 0.25 / 1_000_000
                self.output = 1.25 / 1_000_000
                return
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
        # approximates using cl100k_base
        return super().get_n_tokens(text)

    # override
    def calculate_cost(self, response: object) -> float:
        if response is None:
            raise ValueError("Response is None.")

        i_tokens = response.usage.input_tokens  # type: ignore
        o_tokens = response.usage.output_tokens  # type: ignore

        input_cost = i_tokens * self.input
        output_cost = o_tokens * self.output
        total_cost = input_cost + output_cost

        print(f"\nActual Cost: {i_tokens} + {o_tokens} =  ${total_cost:.2f}")
        return total_cost

    # override
    def _get_completion(self, messages: list, temp: float) -> object:
        load_dotenv()
        client = anthropic.Anthropic()
        return client.messages.create(
            model=self.id,
            max_tokens=4096,
            temperature=temp,
            messages=messages,  # type: ignore
        )

    # override
    def query(self, prompt: Prompt, variable: Variable, temp: float, danger_mode: bool):
        messages = self.build_messages(prompt, variable)
        response = self._get_completion(messages, temp)

        if not danger_mode:
            self.calculate_cost(response)

        return self._parse_completion(response)

    # override
    def _parse_completion(self, response: object) -> str:
        return response.content[0].text  # type: ignore
