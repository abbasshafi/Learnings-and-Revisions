from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os 
from dotenv import find_dotenv,load_dotenv
import warnings
warnings.filterwarnings("ignore")

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"


## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are helpful system. Respond to user queries."),
        ("user","Question:{question}")
    ]
)

## Streamlit framework
st.title("Langchain Demo with Llama2 API ")
input_text=st.text_input("Search the topic you want...")

##  ollama LLama2 LLM
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain= prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))