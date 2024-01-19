import os
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory
import streamlit as st

os.environ['OPENAI_API_KEY'] = "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"

# streamlit framework
st.title("Search Results")
input_text = st.text_input("Search the celebrity you want")

# 1st prompt Templates
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

#Memory
person_memory= ConversationBufferMemory(input_key='name',memory_key='person_memory')
chat_history= ConversationBufferMemory(input_key='person',memory_key='chat_history')
description_memory= ConversationBufferMemory(input_key='dob',memory_key='description_history')

# OpenAI LLMs
llm = OpenAI(temperature=0.8, openai_api_key=os.getenv("OPENAI_API_KEY"))
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True,output_key='person',memory=person_memory)

#2nd Prompt Template
second_input_prompt=PromptTemplate(
    input_variables=['person'],
    template='when was {person} born'
)
chain2=LLMChain(llm=llm,prompt=second_input_prompt,verbose=True, output_key='dob',memory=chat_history)

#3nd Prompt Template
third_input_prompt=PromptTemplate(
    input_variables=['person'],
    template='when was {person} born'
)
chain3=LLMChain(llm=llm,prompt=third_input_prompt,verbose=True, output_key='description',memory=description_memory)

#parent chain
parent_chain=SequentialChain(chains=[chain,chain2],input_variables=['name'],output_variables=['person','dob'],verbose=True)

if input_text:
    st.write(parent_chain({'name':input_text}))

    with st.expander('Person Name'):
        st.info(person_memory.buffer)

    with st.expander("Major Events"):
        st.info(description_memory.buffer)
