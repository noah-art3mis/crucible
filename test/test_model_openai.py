import os
from dotenv import load_dotenv
from crucible.classes.OpenAIModel import OpenAIModel
from crucible.classes.Model import Source
from crucible.classes.Variable import Variable
from crucible.classes.Prompt import Prompt

import pytest


class TestOpenAIModel:
    def test_check_allowed_models_exists(self):
        m = OpenAIModel("gpt-4o")
        assert m

    def test_check_allowed_models_doesnt_exist(self):
        with pytest.raises(ValueError):
            m = OpenAIModel("test")

    def test_check_allowed_models_other_source(self):
        with pytest.raises(ValueError):
            m = OpenAIModel("claude-3-haiku-20240307")

    def test_estimate_costs_positive(self):
        m = OpenAIModel("gpt-4o")
        assert m.estimate_costs(100) > 0

    def test_estimate_costs_negative(self):
        m = OpenAIModel("gpt-4o")
        with pytest.raises(ValueError):
            m.estimate_costs(-100)

    def test_estimate_costs_zero(self):
        m = OpenAIModel("gpt-4o")
        assert m.estimate_costs(0) == 0

    # def test_estimate_costs_null(self):
    #     m = OpenAIModel("gpt-4o")
    #     with pytest.raises(ValueError):
    #         m.estimate_costs(None)

    def test_get_n_tokens_not_empty(self):
        m = OpenAIModel("gpt-4o")
        assert m.get_n_tokens("test") > 0

    def test_get_n_tokens_empty(self):
        m = OpenAIModel("gpt-4o")
        assert m.get_n_tokens("") == 0

    # def testcalculate_cost(self, capsys):
    #     m = OpenAIModel("gpt-4o")
    #     response = {"usage": {"input_tokens": 100, "output_tokens": 200}}
    #     m.calculate_cost(response)
    #     captured = capsys.readouterr()
    #     assert "Actual Cost" in captured.out

    # def testcalculate_cost_null_response(self):
    #     m = OpenAIModel("gpt-4o")
    #     with pytest.raises(ValueError):
    #         m.calculate_cost(None)

    def test_build_messages(self):
        m = OpenAIModel("gpt-4o")
        p = Prompt("test_p", "<variable>", "content <variable> content")
        v = Variable("test_v", "var", ["test_x"])
        actual = m.build_messages(p, v)
        expected = "content var content"
        assert actual == [{"role": "user", "content": expected}]

    def test_completion_not_empty(self):
        load_dotenv()
        m = OpenAIModel("gpt-4o")
        p = Prompt("test_p", "<variable>", "content <variable> content")
        v = Variable("test_v", "var", ["test_x"])
        messages = m.build_messages(p, v)
        assert m._get_completion(messages, 0.0, os.getenv("OPENAI_API_KEY") or "")

    def test_query(self):
        load_dotenv()
        m = OpenAIModel("gpt-4o")
        p = Prompt("test_p", "<variable>", "respond exactly with <|TEST|>")
        v = Variable("test_v", "", ["test_x"])
        r = m.query(p, v, 0.0, os.getenv("OPENAI_API_KEY") or "")
        assert r[0] == "<|TEST|>"
