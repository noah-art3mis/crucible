from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Model:
    id: str


@dataclass(frozen=True)
class Prompt:
    id: str
    slots: str
    content: str


@dataclass(frozen=True)
class Variable:
    id: str
    content: str
    expected: list[str]
    options: list[str]


@dataclass(order=True)
class Result:
    id: str
    model: str
    prompt_id: str
    variable_id: str
    expected: list[str]
    response: str | None = None
    grade: int | None = None
    time_elapsed: float | None = None
    error: str | None = None


@dataclass()
class Task:
    options: list[str] | None
    models: list[Model] | None
    prompts: list[Prompt] | None
    variables: list[Variable] | None
