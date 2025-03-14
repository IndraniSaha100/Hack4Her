from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

load_dotenv()
# Set up Google Generative AI model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def get_genai_response(prompt):
    response = model([HumanMessage(content=prompt)])
    return response.content.strip()

# Streamlit UI
st.title("Chatbot with Streamlit and LangChain")
st.write("Ask me anything!")

# Initialize chat history if not present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get bot response
    bot_response = get_genai_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)