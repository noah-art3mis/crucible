from dataclasses import dataclass


@dataclass(frozen=True)
class Prompt:
    id: str
    slot: str
    content: str
