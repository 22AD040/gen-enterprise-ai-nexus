import streamlit as st
import google.generativeai as genai
from config.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def industry_page():

    st.title("Industry Solution Generator")

    industries = [
        "Healthcare",
        "Finance",
        "Retail",
        "Manufacturing",
        "Education",
        "Telecommunications",
        "Logistics",
        "Energy",
        "Insurance"
    ]

    industry = st.selectbox("Select Industry",industries)

    if st.button("Generate Solutions"):

        with st.spinner("Generating industry insights..."):

            prompt=f"""
You are an enterprise technology strategist.

Provide AI and digital transformation solutions for the {industry} industry.

Structure the response:

Industry Overview
Key Challenges
AI Solutions
Implementation Strategy
Business Impact
"""

            response=model.generate_content(prompt)

            st.write(response.text)