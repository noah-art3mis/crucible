from dataclasses import dataclass


@dataclass(frozen=True)
class Variable:
    id: str
    content: str
    expected: list[str]
    options: list[str] | None = None
