import ollama

from crucible.classes.Model import Model
from crucible.classes.Prompt import Prompt
from crucible.classes.Variable import Variable
from crucible.classes.Model import Source


class LocalModel(Model):
    def __init__(self, id: str):
        super().__init__(id)
        self.source = Source.LOCAL

    def _check_allowed_models(self, id: str) -> None:
        match id:
            case "llama3":
                return
            case _:
                raise ValueError(f"Model {id} not found.")

    # override
    def estimate_costs(self, n_tokens: int) -> float:
        if n_tokens < 0:
            raise ValueError("n_tokens must be a positive integer.")

        return 0.0

    # override
    def get_n_tokens(self, text: str) -> int:
        return super().get_n_tokens(text)

    # override
    def calculate_cost(self, response: object):
        return 0

    # override
    def _get_completion(self, messages: list, temp: float, api_key: None) -> object:
        return ollama.chat(
            model=self.id,
            messages=messages,
            options={"temperature": temp},
        )

    # override
    def query(
        self,
        prompt: Prompt,
        variable: Variable,
        temp: float,
        api_key: None,
    ):
        messages = self.build_messages(prompt, variable)
        response = self._get_completion(messages, temp, api_key)

        completion = self._parse_completion(response)
        costs = self.calculate_cost(response)

        return completion, costs

    # override
    def _parse_completion(self, response: object) -> str:
        return response["message"]["content"]  # type: ignore
