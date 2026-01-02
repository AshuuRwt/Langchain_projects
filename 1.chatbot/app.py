import streamlit as st
import os

# Load secrets
os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]
os.environ["LANGCHAIN_PROJECT"] = st.secrets["LANGCHAIN_PROJECT"]
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
os.environ["LANGCHAIN_TRACING_V2"] = st.secrets["LANGCHAIN_TRACING_V2"]

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# Streamlit UI
st.title("Gemini 2.5 Flash Chatbot 🤖")
input_text = st.text_input("Ask a question:")

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.environ["GOOGLE_API_KEY"]
)

# LangChain prompt setup
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Question: {question}")
])

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Generate response
if input_text:
    st.write("Processing...")
    response = chain.invoke({"question": input_text})
    st.subheader("Answer:")
    st.write(response)
