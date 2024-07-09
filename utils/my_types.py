from dataclasses import dataclass


@dataclass(frozen=True)
class BaseEntity:
    id: str


@dataclass(frozen=True)
class Model(BaseEntity):
    source: str  # local | openai | anthropic


@dataclass(frozen=True)
class Prompt(BaseEntity):
    slot: str
    content: str


@dataclass(frozen=True)
class Variable(BaseEntity):
    content: str
    expected: list[str]
    options: list[str] | None


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
