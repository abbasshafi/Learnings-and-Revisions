from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# parsing string outputs: the process of extracting relevant information or structure from a string of text.

import streamlit as st
import os 
from dotenv import load_dotenv

os.environ["OPENAI_API_kEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]='true'
os.environ["LANGCHAIN_API_key"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are helpful system. Respond to user queries."),
        ("user","Question:{question}")
    ]
)

## Streamlit framework
st.title("Langchain Demo with OpenAI API ")
input_text=st.text_input("Search the topic you want...")

## OpenAI LLM
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt | llm | output_parser


if input_text:
    st.write(chain.invoke({"question": input_text}))