import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "GEN Enterprise AI NEXUS"

BACKGROUND = "https://plus.unsplash.com/premium_photo-1673637379460-8ee1ec6d219c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

LOGO = "https://cdn-icons-png.flaticon.com/128/18648/18648894.png"



try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")