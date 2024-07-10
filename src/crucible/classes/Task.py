from dataclasses import dataclass
from crucible.classes.Model import Model
from crucible.classes.Prompt import Prompt
from crucible.classes.Variable import Variable


@dataclass(frozen=True)
class Task:
    run_id: str
    task_id: str
    model: Model
    prompt: Prompt
    variable: Variable
    expected: list[str]
