from fastapi import FastAPI
from langchain.prompt import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os 
