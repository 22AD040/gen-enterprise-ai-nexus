import streamlit as st
import google.generativeai as genai
from config.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def recommender_page():

    st.title("AI Solution Recommender")

    st.markdown("""
### How This System Works

Organizations often face complex operational problems.
This AI analyzes your description and recommends strategic solutions.

**Input**

Describe a business challenge.

Example:

"Our company manages thousands of internal documents such as policies and reports. Employees struggle to quickly find relevant information."

**Output**

• Recommended AI solutions  
• Implementation approach  
• Expected benefits
""")

    problem = st.text_area("Describe your business challenge")

    if st.button("Generate Recommendations"):

        with st.spinner("Analyzing business scenario..."):

            prompt=f"""
You are an enterprise AI consultant.

Analyze the following business challenge and provide a structured solution.

Return results in this format:

Problem Summary:
Recommended Solutions:
Implementation Strategy:
Expected Benefits:

Business Challenge:
{problem}
"""

            response=model.generate_content(prompt)

            st.success("AI Recommendations")

            st.write(response.text)