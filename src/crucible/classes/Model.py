from enum import Enum, auto
from abc import ABC, abstractmethod

import tiktoken
import ollama
import anthropic
from openai import OpenAI
from dotenv import load_dotenv

from crucible.classes.Prompt import Prompt
from crucible.classes.Variable import Variable


class Source(Enum):
    OPENAI = auto()
    ANTHROPIC = auto()
    LOCAL = auto()


class Model(ABC):

    def __init__(self, id: str) -> None:
        super().__init__()
        self.id = id

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
    def _get_actual_costs(self, response: object) -> None:
        pass

    @abstractmethod
    def _get_completion(self) -> str:
        pass

    @abstractmethod
    def _parse_completion(self, response: object) -> str:
        pass

    @abstractmethod
    def query(
        self, prompt: Prompt, variable: Variable, temp: float, danger_mode: bool
    ) -> str:
        pass

    def build_messages(
        self, prompt: Prompt, variable: Variable
    ) -> list[dict[str, str]]:
        # TODO
        text = prompt.content.replace(prompt.slot, variable.content)
        return [{"role": "user", "content": text}]


class OpenAIModel(Model):
    def __init__(self, id: str) -> None:
        super().__init__(id)
        self.source = Source.OPENAI
        self.omni_input = 5.0 / 1_000_000
        self.omni_output = 15.0 / 1_000_000

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


class AnthropicModel(Model):
    def __init__(self, id: str):
        super().__init__(id)
        self.source = Source.ANTHROPIC
        self.haiku_input = 0.25 / 1_000_000
        self.haiku_output = 1.25 / 1_000_000

    # override
    def estimate_costs(self, n_tokens: int) -> float:
        input_cost = n_tokens * self.haiku_input
        output_cost = n_tokens * self.haiku_output
        total_cost = input_cost + output_cost
        return total_cost

    # override
    def get_n_tokens(self, text: str) -> int:
        return super().get_n_tokens(text)

    # override
    def _get_actual_costs(self, response: object) -> None:
        i_tokens = response.usage.input_tokens  # type: ignore
        o_tokens = response.usage.output_tokens  # type: ignore

        input_cost = i_tokens * self.haiku_input
        output_cost = o_tokens * self.haiku_output
        total_cost = input_cost + output_cost

        print(f"\nActual Cost: {i_tokens} + {o_tokens} =  ${total_cost:.2f}")

    # override
    def _get_completion(self, messages: list, temp: float) -> object:
        load_dotenv()
        client = anthropic.Anthropic()
        return client.messages.create(
            model=self.id,
            max_tokens=4096,
            temperature=0,
            messages=messages,  # type: ignore
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
        return response.content[0].text  # type: ignore


class LocalModel(Model):
    def __init__(self, id: str):
        super().__init__(id)
        self.source = Source.LOCAL

    # override
    def estimate_costs(self, n_tokens: int) -> float:
        return 0.0

    # override
    def get_n_tokens(self, text: str) -> int:
        return super().get_n_tokens(text)

    # override
    def _get_actual_costs(self, response: object):
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
            self._get_actual_costs(response)

        return self._parse_completion(response)

    # override
    def _parse_completion(self, response: object) -> str:
        return response["message"]["content"]  # type: ignore