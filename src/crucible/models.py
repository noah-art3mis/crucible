from src.crucible.classes.Model import Model
from crucible.classes.AnthropicModel import AnthropicModel
from src.crucible.classes.LocalModel import LocalModel
from src.crucible.classes.OpenAIModel import OpenAIModel

models_: list[Model] = [
    OpenAIModel("gpt-4o"),
    AnthropicModel("claude-3-haiku-20240307"),
    LocalModel("llama3"),
]
