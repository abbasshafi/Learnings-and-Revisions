##Integrate our code OpenAI API

import os
from constants import OPENAI_API_KEY
from langchain.llms import OpenAI
import streamlit as st

#to initialize streamlit framework
st.title("Langchain Demo with OpenAI")
input_text=st.text_input("Search the topic u want")

##OpenAI LLMs
llm = OpenAI(temperature=0.8, openai_api_key="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")
# llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))