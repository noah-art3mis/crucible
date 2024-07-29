import streamlit as st
from crucible.utils.grading import GradingType
from crucible.classes.Runner import Runner
from crucible.classes.Model import Source
from crucible.classes.Prompt import Prompt
from crucible.classes.Variable import Variable
from crucible.classes.OpenAIModel import OpenAIModel
from crucible.classes.AnthropicModel import AnthropicModel

available_models = [
    {"name": "gpt-4o-mini", "source": Source.OPENAI},
    {"name": "claude-3-haiku-20240307", "source": Source.ANTHROPIC},
    {"name": "gpt-4o", "source": Source.OPENAI},
]

available_gradings = [GradingType.EXACT, GradingType.QUALITATIVE]

danger_mode = True  # always true

st.title("Crucible")
st.caption("Lightweight prompt evaluation")
st.caption("An AUTOMATON tool")

st.markdown("---")
st.subheader("Configuration")

with st.expander("Models"):

    selected_models = st.multiselect(
        "Select models",
        available_models,
        format_func=lambda x: x["name"],
        default=available_models[0],
    )

    st.write("---")

    st.caption(
        "We do not store any data whatsoever. (At least I don't; I don't know about streamlit.)"
    )
    openai_api_key = st.text_input("OpenAI API key", type="password")
    anthropic_api_key = st.text_input("Anthropic API key", type="password")

    models = []
    for model_info in selected_models:
        name = model_info["name"]
        source = model_info["source"]
        if source == Source.OPENAI:
            models.append(OpenAIModel(name))
        if source == Source.ANTHROPIC:
            models.append(AnthropicModel(name))


with st.expander("Prompts"):
    n_prompts = st.number_input("Number of prompts", min_value=1, max_value=20, value=1)
    prompts = []
    for i in range(int(n_prompts)):
        st.markdown("---")

        st.write("Prompt:")
        prompt_id = st.text_input("Name", f"prompt_{i + 1}", key=f"prompt_id_{i}")
        prompt_slot = st.text_input("Slot", "{variable}", key=f"slot_{i}")
        prompt_content = st.text_input(
            "Content",
            "Considering this context, respond with yes or no ### Context: {variable}. Is this true?",
            key=f"content_{i}",
        )
        prompts.append(Prompt(prompt_id, prompt_slot, prompt_content))


with st.expander("Variable"):
    n_var = st.number_input("Number of variables", min_value=1, max_value=20, value=2)
    variables = []
    for i in range(int(n_var)):
        st.markdown("---")

        st.write("Variable:")

        variable_id = st.text_input("Name", f"variable_{i + 1}", key=f"var_id_{i}")
        variable_content = st.text_input(
            "Content",
            "Geckos manipulate vacuum energy to stick to walls",
            key=f"var_content_{i}",
        )
        variable_expected = st.text_input(
            "Expected value", "yes", key=f"var_expected_{i}"
        )
        variables.append(Variable(variable_id, variable_content, [variable_expected]))


st.markdown("---")
st.subheader("Other configs")
grading_type = st.selectbox(
    "Select grading type", available_gradings, format_func=lambda x: x.name
)
temperature = st.slider("Select temperature", 0.0, 1.0, 0.0, 0.2)

st.markdown("---")
if st.button("Compile"):

    st.subheader("Summary:")

    runner = Runner(
        models=models,
        prompts=prompts,
        variables=variables,
        grading_type=grading_type,  # type: ignore
        danger_mode=danger_mode,
        temperature=temperature,
        openai_api_key=openai_api_key,
        anthropic_api_key=anthropic_api_key,
    )
    estimated_costs = runner.estimate_all_costs()

    st.write("Models")
    for model in runner.models:
        st.write(f"- {model.id}")

    st.write("Prompts")
    for prompt in runner.prompts:
        st.write(f"- {prompt.id}")

    st.write("Variables")
    for variable in runner.variables:
        st.write(f"- {variable.id}")

    st.write(f"Grading Type: {runner.grading_type}")
    st.write(f"Temperature: {runner.temperature}")
    st.write()
    st.write(f"Total cases: {len(runner.tasks)}")
    st.write(f"Estimated costs: ${estimated_costs:.2f} USD")

    if estimated_costs > 1.00:
        st.warning("Are you sure?")

    if st.button("Run"):
        for i, task in enumerate(runner.tasks):
            st.progress(i)
            runner.run_task(task)


# st.download_button("Download report", file)
