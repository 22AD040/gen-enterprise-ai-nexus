import streamlit as st

from config.config import BACKGROUND, LOGO
from auth.auth_ui import auth_page

from modules.semantic_search import semantic_search_page
from modules.dashboard import dashboard_page
from modules.chatbot import chatbot_page
from modules.recommender import recommender_page
from modules.blog_assistant import blog_assistant_page
from modules.industry_generator import industry_page




st.set_page_config(
    page_title="GEN Enterprise AI NEXUS",
    layout="wide",
    page_icon="🤖"
)




st.markdown(
f"""
<style>

/* -----------------------------
BACKGROUND
----------------------------- */

.stApp {{
    background-image: linear-gradient(
        rgba(0,0,0,0.55),
        rgba(0,0,0,0.55)
    ),
    url("{BACKGROUND}");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}


/* -----------------------------
REMOVE WHITE BOX ABOVE TITLE
----------------------------- */

.block-container {{
    padding-top:30px;
    background:transparent !important;
    box-shadow:none !important;
}}


/* -----------------------------
SIDEBAR
----------------------------- */

[data-testid="stSidebar"] {{
    background: rgba(0,0,0,0.92);
}}

[data-testid="stSidebar"] * {{
    color:white !important;
}}


/* -----------------------------
HEADINGS STYLE
----------------------------- */

h1{{
    font-size:42px !important;
    font-weight:800 !important;
    color:#ffffff !important;
}}

h2{{
    font-size:30px !important;
    font-weight:700 !important;
    color:#ffffff !important;
}}

h3{{
    font-size:22px !important;
    font-weight:700 !important;
    color:#ffffff !important;
}}


/* -----------------------------
NORMAL TEXT (BRIGHT WHITE)
----------------------------- */

p, span {{
    color:#ffffff !important;
    font-weight:600 !important;
}}


/* -----------------------------
PROCESSING STEPS TEXT (DARK BLACK)
----------------------------- */

li {{
    color:#4db8ff !important;
    font-weight:800 !important;
}}


/* -----------------------------
AI GENERATED OUTPUT TEXT
----------------------------- */

.markdown-text-container p {{
    color:#ffffff !important;
    font-weight:800 !important;
}}

.markdown-text-container li {{
    color:#00ff9d !important;
    font-weight:800 !important;
}}

.markdown-text-container h2 {{
    color:#4db8ff !important;
    font-weight:800 !important;
}}

.markdown-text-container li {{
    color:#ffffff !important;
    font-weight:700 !important;
}}


/* -----------------------------
INPUT TEXT
----------------------------- */

.stTextInput input {{
    color:#ffffff !important;
    font-weight:700 !important;
    background-color:rgba(0,0,0,0.65) !important;
}}

textarea {{
    color:#ffffff !important;
    font-weight:700 !important;
    background-color:rgba(0,0,0,0.65) !important;
}}

select {{
    color:#ffffff !important;
    font-weight:700 !important;
}}

/* placeholder text */

::placeholder {{
    color:#cbd5f5 !important;
    font-weight:600;
}}


/* -----------------------------
FILE UPLOADER TEXT
----------------------------- */

[data-testid="stFileUploader"] label {{
    color:#000000 !important;
    font-weight:800 !important;
}}

[data-testid="stFileUploader"] div {{
    color:#000000 !important;
    font-weight:700 !important;
}}

[data-testid="stFileUploader"] span {{
    color:#000000 !important;
    font-weight:700 !important;
}}

[data-testid="stFileUploader"] p {{
    color:#000000 !important;
    font-weight:700 !important;
}}

[data-testid="stFileUploader"] button {{
    color:#000000 !important;
    font-weight:700 !important;
}}

[data-testid="stFileUploader"] small {{
    color:#000000 !important;
}}

[data-testid="stFileUploader"] {{
    border:2px dashed #38bdf8;
    border-radius:10px;
    padding:10px;
}}

/* -----------------------------
BUTTON STYLE
----------------------------- */

.stButton button {{
    background: linear-gradient(90deg,#00c6ff,#0072ff);
    color:white;
    border-radius:8px;
    border:none;
    padding:8px 18px;
    font-weight:600;
}}

.stButton button:hover {{
    background: linear-gradient(90deg,#00ff9d,#00c6ff);
}}

</style>
""",
unsafe_allow_html=True
)


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False




if not st.session_state.logged_in:

    auth_page()

else:

    st.sidebar.image(LOGO, width=90)

    st.sidebar.markdown(
        """
        ## GEN Enterprise AI Nexus
        Enterprise GenAI Intelligence Platform
        """
    )

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Semantic Search",
            "Recommender",
            "Chatbot",
            "Industry Generator",
            "Blog Assistant"
        ]
    )

    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.rerun()

    if page == "Dashboard":
        dashboard_page()

    elif page == "Semantic Search":
        semantic_search_page()

    elif page == "Recommender":
        recommender_page()

    elif page == "Chatbot":
        chatbot_page()

    elif page == "Industry Generator":
        industry_page()

    elif page == "Blog Assistant":
        blog_assistant_page()