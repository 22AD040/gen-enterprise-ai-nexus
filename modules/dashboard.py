import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def dashboard_page():

    st.title("Enterprise Intelligence Dashboard")

    st.markdown("""
### Platform Overview

This dashboard demonstrates how enterprise technologies are adopted and how AI-driven analytics can help organizations make better decisions.

**Input Data**

• Technology adoption metrics  
• Enterprise operational datasets  
• Simulated analytics data  

**Outputs**

• Visual dashboards  
• Technology adoption insights  
• Business intelligence trends  

The graphs below illustrate how organizations typically distribute investments across emerging technologies.
""")

    tech = ["Artificial Intelligence","Cloud Computing","Automation","Internet of Things","Data Science"]

    values = np.random.randint(20,100,5)

    df = pd.DataFrame({
        "Technology":tech,
        "Adoption":values
    })

    col1,col2 = st.columns(2)

    fig1 = px.bar(
        df,
        x="Technology",
        y="Adoption",
        title="Enterprise Technology Adoption Levels"
    )

    col1.plotly_chart(fig1,use_container_width=True)

    col1.markdown("""
**Explanation**

This chart shows how different technologies are adopted within enterprises.

Higher bars indicate stronger adoption and investment. For example:

• AI often drives automation and predictive analytics  
• Cloud supports scalable infrastructure  
• IoT enables real-time monitoring
""")

    fig2 = px.pie(
        df,
        names="Technology",
        values="Adoption",
        title="Technology Distribution Across Enterprise Systems"
    )

    col2.plotly_chart(fig2,use_container_width=True)

    col2.markdown("""
**Explanation**

This pie chart illustrates how enterprise technology resources are distributed.

A balanced distribution indicates diversified innovation strategies.
""")

    st.subheader("Enterprise Data Distribution Simulation")

    data = np.random.randn(300)

    fig3 = px.histogram(data,title="Enterprise Data Pattern Distribution")

    st.plotly_chart(fig3,use_container_width=True)

    st.markdown("""
**Explanation**

This histogram simulates enterprise data variation.

Understanding such distributions helps organizations detect anomalies,
forecast trends, and build predictive machine learning models.
""")