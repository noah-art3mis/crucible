from crucible.utils.my_types import Model

models_: list[Model] = [
    # Model("llama3", "local"),
    Model("gpt-4o", "openai"),
    Model("claude-3-haiku-20240307", "anthropic"),
]
