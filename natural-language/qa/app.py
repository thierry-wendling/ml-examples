from pip import main
import streamlit as st
from transformers import pipeline

MODEL_NAME = 'distilbert-base-cased-distilled-squad'


@st.cache(allow_output_mutation=True)
def get_question_answerer():
    return pipeline("question-answering", model=MODEL_NAME)


if __name__ == '__main__':

    st.title('Question answering')

    with st.form(key="my_form"):
        question_answerer = get_question_answerer()
        question = st.text_area(
            "Question",
            height=510,
        )
        context = st.text_area(
            "Context",
            height=510,
        )
        submitted = st.form_submit_button(label='Compute')
        if submitted:
            result = question_answerer(question, context)
            st.write(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")
