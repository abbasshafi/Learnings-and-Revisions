import os
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate
from langchain.chains import SimpleSequentialChain
import streamlit as st

os.environ['OPENAI_API_KEY'] = "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"

# streamlit framework
st.title("Search Results")
input_text = st.text_input("Search the celebrity you want")

# prompt Templates
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

# OpenAI LLMs
llm = OpenAI(temperature=0.8, openai_api_key=os.getenv("OPENAI_API_KEY"))
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True,output_key='person')

second_input_prompt=PromptTemplate(
    input_variables=['person'],
    template='when was {person} born'
)

chain2=LLMChain(llm=llm,second_input_prompt,verbose=True, output_key='dob')

parent_chain=SimpleSequentialChain(chains=[chain,chain2],verbose=True)

if input_text:
    st.write(chain(input_text))
