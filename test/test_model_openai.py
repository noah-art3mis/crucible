from src.crucible.classes.OpenAIModel import OpenAIModel
from src.crucible.classes.Model import Source
from src.crucible.classes.Variable import Variable
from src.crucible.classes.Prompt import Prompt

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

    # def test_print_actual_costs(self, capsys):
    #     m = OpenAIModel("gpt-4o")
    #     response = {"usage": {"input_tokens": 100, "output_tokens": 200}}
    #     m._print_actual_costs(response)
    #     captured = capsys.readouterr()
    #     assert "Actual Cost" in captured.out

    # def test_print_actual_costs_null_response(self):
    #     m = OpenAIModel("gpt-4o")
    #     with pytest.raises(ValueError):
    #         m._print_actual_costs(None)

    def test_build_messages(self):
        m = OpenAIModel("gpt-4o")
        p = Prompt("test_p", "<variable>", "content <variable> content")
        v = Variable("test_v", "var", ["test_x"])
        actual = m.build_messages(p, v)
        expected = "content var content"
        assert actual == [{"role": "user", "content": expected}]

    def test_completion_not_empty(self):
        m = OpenAIModel("gpt-4o")
        p = Prompt("test_p", "<variable>", "content <variable> content")
        v = Variable("test_v", "var", ["test_x"])
        messages = m.build_messages(p, v)
        assert m._get_completion(messages, 0.0)

    def test_query(self):
        m = OpenAIModel("gpt-4o")
        p = Prompt("test_p", "<variable>", "respond exactly with <|TEST|>")
        v = Variable("test_v", "", ["test_x"])
        r = m.query(p, v, 0.0, False)
        assert r == "<|TEST|>"
