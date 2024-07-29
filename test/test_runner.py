from dotenv import load_dotenv
from crucible.classes.AnthropicModel import AnthropicModel
from crucible.utils.grading import GradingType
from crucible.classes.OpenAIModel import OpenAIModel
from crucible.classes.Model import Source
from crucible.classes.Variable import Variable
from crucible.classes.Prompt import Prompt
from crucible.classes.Runner import Runner
import os
import pytest


class TestRunner:
    def test_init_1(self):
        m = [
            OpenAIModel("gpt-4o"),
            AnthropicModel("claude-3-haiku-20240307"),
        ]

        p = [
            Prompt(id="test_prompt_1", slot="{variable}", content="teste: {variable}"),
            Prompt(id="test_prompt_2", slot="{slot}", content="teste2: {slot}"),
        ]

        v = [
            Variable(id="teste_variable_1", content="VARIABLE_1", expected=["OK"]),
            Variable(id="teste_variable_2", content="VARIABLE_2", expected=["OK"]),
        ]

        load_dotenv()
        runner = Runner(
            models=m,
            prompts=p,
            variables=v,
            grading_type=GradingType.EXACT,
            danger_mode=True,
            temperature=0.0,
            openai_api_key=os.getenv("OPENAI_API_KEY") or "",
            anthropic_api_key=os.getenv("ANTHROPIC_API_KEY") or "",
        )

        assert len(runner.tasks) == 8

    # def test_calculate_costs_0(self):
    #     printer.calculate_costs_all()


# variable change name
# gradint type
