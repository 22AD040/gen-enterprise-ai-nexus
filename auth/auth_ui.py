import streamlit as st
from auth.auth_db import register_user, login_user
from config.config import LOGO


def auth_page():

    st.markdown("""
    <style>

    .login-title{
        color:#3aa0ff;
        font-size:56px;
        font-weight:800;
        text-align:center;
        margin-bottom:25px;
    }

    input{
        color:white !important;
        font-weight:700 !important;
        background-color:rgba(0,0,0,0.65) !important;
    }

    label{
        color:white !important;
        font-weight:700 !important;
    }

    ::placeholder{
    color:#cbd5f5 !important;
    }

    /* focus effect */

    input:focus{
        border:2px solid #38bdf8 !important;
    }

    </style>
    """, unsafe_allow_html=True)


    col1, col2, col3 = st.columns([1.5,1,1.5])

    with col2:
        
        st.markdown("<br><br>", unsafe_allow_html=True)

        l1, l2, l3 = st.columns([1,1,1])
        with l2:
            st.image(LOGO, width=220)

        # TITLE
        st.markdown(
            "<div class='login-title'>GEN Enterprise AI Nexus</div>",
            unsafe_allow_html=True
        )

        option = st.radio("Select Option", ["Login", "Register"])

        if option == "Register":
            full_name = st.text_input("Full Name")

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if option == "Register":

            if st.button("Create Account", use_container_width=True):

                if register_user(email, password):
                    st.success("Account created successfully")
                else:
                    st.error("User already exists")

        else:

            if st.button("Login", use_container_width=True):

                if login_user(email, password):

                    st.session_state.logged_in = True
                    st.session_state.user = email
                    st.rerun()

                else:
                    st.error("Invalid credentials")