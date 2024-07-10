from crucible.classes.Model import OpenAIModel, AnthropicModel, LocalModel, Model

models_: list[Model] = [
    OpenAIModel("gpt-4o"),
    AnthropicModel("claude-3-haiku-20240307"),
    LocalModel("llama3"),
]
