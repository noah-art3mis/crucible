from dataclasses import dataclass
from crucible.classes.Task import Task


@dataclass(frozen=True)
class Result:
    task: Task
    response: str | None
    grade: int | None
    info: str | None
    time_elapsed: float | None = None
    error: str | None = None
