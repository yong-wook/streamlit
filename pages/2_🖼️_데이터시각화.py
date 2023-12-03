import streamlit as st
import webbrowser
from streamlit_extras.switch_page_button import switch_page

if "auth_login" not in st.session_state:
   st.session_state["auth_login"] = None 

if st.session_state["auth_login"] != "로그인 중":
    switch_page("home")
    

st.header("데이터 시각화 연습용")
st.sidebar.success(st.session_state["auth_login"])
