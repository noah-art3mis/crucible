from enum import Enum, auto
from abc import ABC, abstractmethod

import tiktoken

from crucible.classes.Prompt import Prompt
from crucible.classes.Variable import Variable


class Source(Enum):
    OPENAI = auto()
    ANTHROPIC = auto()
    LOCAL = auto()


class Model(ABC):

    def __init__(self, id: str) -> None:
        super().__init__()
        self._check_allowed_models(id)
        self.id = id
        self.source = None

    @abstractmethod
    def _check_allowed_models(self, id: str) -> None:
        pass

    @abstractmethod
    def estimate_costs(self, n_tokens: int) -> float:
        pass

    @abstractmethod
    def get_n_tokens(self, text: str) -> int:
        encoding = tiktoken.get_encoding("cl100k_base")
        tokenized = encoding.encode(text)
        n_tokens = len(tokenized)
        return n_tokens

    @abstractmethod
    def calculate_cost(self, response: object) -> float:
        pass

    @abstractmethod
    def _get_completion(self, messages: list, temp: float, api_key: str) -> str:
        pass

    @abstractmethod
    def _parse_completion(self, response: object) -> str:
        pass

    @abstractmethod
    def query(
        self,
        prompt: Prompt,
        variable: Variable,
        temp: float,
        api_key: str | None,
        danger_mode: bool,
    ) -> str:
        pass

    def build_messages(
        self, prompt: Prompt, variable: Variable
    ) -> list[dict[str, str]]:
        # TODO
        text = prompt.content.replace(prompt.slot, variable.content)
        return [{"role": "user", "content": text}]
