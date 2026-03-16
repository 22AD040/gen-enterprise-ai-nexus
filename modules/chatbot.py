import streamlit as st
import google.generativeai as genai
from config.config import GEMINI_API_KEY
from utils.chat_memory import load_history, add_message

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def chatbot_page():

    st.title("Enterprise Knowledge Chatbot")

    st.markdown("""
### How this AI Assistant Works

**Input:**  
Users ask enterprise or technical questions.

**Processing Steps**

1. User query sent to Gemini AI  
2. AI analyzes enterprise context  
3. Generates structured response  

**Output:**  
Clear explanation with enterprise insights.
""")

    history = load_history()

    user_input = st.chat_input("Ask an enterprise question")

    if user_input:

        with st.spinner("AI thinking..."):

            response = model.generate_content(user_input)

            answer = response.text

            add_message(user_input, answer)

            history.append({
                "user": user_input,
                "assistant": answer
            })

    for chat in history:

        st.chat_message("user").write(chat["user"])
        st.chat_message("assistant").write(chat["assistant"])