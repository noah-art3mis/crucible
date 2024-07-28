from crucible.classes.Model import Model
from crucible.classes.AnthropicModel import AnthropicModel
from crucible.classes.LocalModel import LocalModel
from crucible.classes.OpenAIModel import OpenAIModel

models_: list[Model] = [
    OpenAIModel("gpt-4o-mini"),
    AnthropicModel("claude-3-haiku-20240307"),
    # LocalModel("llama3"),
]
