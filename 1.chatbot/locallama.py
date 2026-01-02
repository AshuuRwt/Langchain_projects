from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the queries."),
    ("user", "Question: {question}")
])

st.title("LangChain AI 🤖")
st.write("✅ Streamlit UI loaded")

input_text = st.text_input("Search the topic you want:")

# NEW OLLAMA CLIENT
llm = OllamaLLM(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write("Processing your query...")
    response = chain.invoke({"question": input_text})
    st.subheader("Answer:")
    st.write(response)
