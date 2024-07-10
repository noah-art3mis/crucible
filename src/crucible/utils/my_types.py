from dataclasses import dataclass
from crucible.utils.Model import Model


@dataclass(frozen=True)
class Prompt:
    slot: str
    content: str


@dataclass(frozen=True)
class Variable:
    content: str
    expected: list[str]
    options: list[str] | None = None


@dataclass(order=True)
class Result:
    run_id: str
    case_id: str
    model_id: str
    prompt_id: str
    variable_id: str
    expected: list[str]
    response: str | None = None
    grade: int | None = None
    info: str | None = None
    time_elapsed: float | None = None
    error: str | None = None


class Report:
    def __init__(self):
        self.header: str = ""
        self.results: list[Result] = []


@dataclass()
class Task:
    options: list[str] | None
    models: list[Model] | None
    prompts: list[Prompt] | None
    variables: list[Variable] | None
