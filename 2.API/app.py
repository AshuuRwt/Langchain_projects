from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A Simple API Server"
)

@app.get("/")
def home():
    return {"message": "LangChain API Server is running"}

add_routes(app, ChatOpenAI(), path="/openai")

model = ChatOpenAI()

llm = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template(
    "Write me an assay about {topic} around with 100 words"
)
prompt2 = ChatPromptTemplate.from_template(
    "Write me an poem about {topic} around with 100 words"
)

add_routes(app, prompt1 | model, path="/essay")
add_routes(app, prompt2 | llm, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
