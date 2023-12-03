import streamlit as st
import webbrowser

if st.session_state["auth_login"] != "로그인 중":
    webbrowser.open("https://usewookstest.streamlit.app/")

st.header("각종 크롤러 연습용")
st.sidebar.success(st.session_state["auth_login"])
