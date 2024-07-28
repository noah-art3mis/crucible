from dataclasses import dataclass


@dataclass
class Result:
    response: str | None
    grade: int
    info: str
    actual_cost: float | None
    time_elapsed: float | None
