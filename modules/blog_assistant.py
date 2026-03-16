import streamlit as st
import google.generativeai as genai
from config.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def blog_assistant_page():

    st.title("Blog Research Assistant")

    st.markdown("""
### How This Tool Works

This assistant analyzes long blog content and extracts key insights.

**Input**

Paste a blog article.

**Processing**

The AI analyzes context, structure, and themes.

**Output**

• Main topic  
• Key insights  
• Important concepts
""")

    blog_text = st.text_area("Paste blog text")

    question = st.text_input("Ask about the blog")

    if st.button("Analyze Blog"):

        with st.spinner("Analyzing blog content..."):

            prompt=f"""
Analyze the following blog content.

Return structured analysis:

Main Topic:
Key Points:
Important Insights:

Blog:
{blog_text}

Question:
{question}
"""

            response=model.generate_content(prompt)

            st.write(response.text)