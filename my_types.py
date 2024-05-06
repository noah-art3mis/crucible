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
    expected: str
    options: list[str]


@dataclass(order=True)
class Result:
    id: str
    model: str
    prompt_id: str
    variable_id: str
    expected: str
    response: Optional[str]
    grade: int
    time_elapsed: float
    error: Optional[str]
