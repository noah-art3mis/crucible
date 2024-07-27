import ollama

from src.crucible.classes.Model import Model
from src.crucible.classes.Prompt import Prompt
from src.crucible.classes.Variable import Variable
from src.crucible.classes.Model import Source


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
    def _print_actual_costs(self, response: object):
        print(f"Actual Cost: actually free!")

    # override
    def _get_completion(self, messages: list, temp: float) -> object:
        return ollama.chat(
            model=self.id,
            messages=messages,
            options={"temperature": temp},
        )

    # override
    def query(self, prompt: Prompt, variable: Variable, temp: float, danger_mode: bool):
        messages = self.build_messages(prompt, variable)
        response = self._get_completion(messages, temp)

        if not danger_mode:
            self._print_actual_costs(response)

        return self._parse_completion(response)

    # override
    def _parse_completion(self, response: object) -> str:
        return response["message"]["content"]  # type: ignore
