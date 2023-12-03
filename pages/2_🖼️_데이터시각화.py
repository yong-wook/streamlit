import streamlit as st
import webbrowser


if st.session_state["auth_login"] != "로그인 중":
    webbrowser.open("http://localhost:8501")
    

st.header("데이터 시각화 연습용")
st.sidebar.success(st.session_state["auth_login"])