from crucible.classes.Model import Model
from crucible.classes.Prompt import Prompt
from crucible.classes.Variable import Variable
from crucible.classes.Report import Result

from dataclasses import dataclass, field


@dataclass
class Task:
    id: str
    model: Model
    prompt: Prompt
    variable: Variable
    expected: list[str]
    estimated_cost: float = field(init=False)
    result: Result | None = None

    def __post_init__(self):
        self.estimated_cost = self._estimate_costs()

    def _estimate_costs(self) -> float:
        messages = self.model.build_messages(self.prompt, self.variable)
        n_tokens = self.model.get_n_tokens(str(messages))
        return self.model.estimate_costs(n_tokens)
