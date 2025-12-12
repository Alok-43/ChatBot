from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import warnings
import config  # This loads all environment variables

warnings.filterwarnings('ignore')

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "I am chatbot. I am here to assist you. Please type your queries"),
        ("user", "Question:{question}")
    ]
)

# Streamlit UI Configuration
st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Streamlit framework
st.title('🤖 Custom Gemini Chatbot by Alok')


input_text = st.text_input("How may I help you?", placeholder="Type your question here...")

# Google Gemini LLM with LangSmith tracking
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    with st.spinner('Thinking...'):
        try:
            response = chain.invoke({'question': input_text})
            st.success("Response:")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("Please check your API keys in the .env file")

# Sidebar information
with st.sidebar:
    st.header("About")
    st.info("""
    This chatbot uses:
    - Google Gemini 2.5 Flash
    - LangChain Framework
    - Streamlit UI
    """)
    st.header("Settings")
    st.write(f"Model: gemini-2.5-flash")
    st.write(f"Temperature: 0.7")
