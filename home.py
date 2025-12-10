import streamlit as st
from app.db import get_db_connection
from main import validate_password, hash_password
from app.users import add_user, get_user


conn = get_db_connection()

st.header('Welcome !!!')

if "logged_in not in" not in st.session_state:
    st.session_state["logged_in"]=False

if st.button("log in") :
    st.session_state["logged_in"]=True
    st.success("you are now logged in")

tab_login, tab_register = st.tabs(["login","register"])

with tab_login:
    login_username = st.text_input("Username")
    login_password = st.text_input("password", type="password")


with tab_register:
    register_username=st.text_input("new username")
    register_password=st.text_input("new password",type="password")
