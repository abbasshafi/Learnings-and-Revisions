from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os 
from langchain_community.llms import ollama

os.environ["OPENAI_API_KEY"]=""

app = FastAPI(
    title="Langchain Server",
    description="A Simple API Server",
    version="1.0"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
model= ChatOpenAI()

llm=ollama(model="llama2")

prompt1=ChatPromptTemplate.from_template("Write me an essay {topic} with only 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an peom {topic} with only 100 words")

add_routes(
    app,
    prompt1 | model,
    path="/essay"
)
add_routes(
    app,
    prompt2 | llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)