import streamlit as st
import streamlit_authenticator as sa
from pathlib import Path
import pickle

st.set_page_config (
    page_title="Use Wook`s Paradise",
    page_icon="👍"
)
################ 유저 인증
username =["이용욱","김성은"]
name = ["zealot","nanjangi"]

######### 비번 로드
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_password= pickle.load(file)
credentials = {"usernames":{}}
for un, name, pw in zip(name, username, hashed_password):
        user_dict = {"name":name,"password":pw}
        credentials["usernames"].update({un:user_dict})


auth = sa.Authenticate(credentials, "myfirstcookie", "adfsdf", cookie_expiry_days=0)
name, auth_status, username = auth.login("Login","main")

if auth_status == False:
    st.error("아이디/비번이 틀렸슴다.")
    st.session_state["auth_login"] = None

if auth_status == None:
    st.warning("뭐라도 입력 하시죠. 암것도 없잖소")
    st.session_state["auth_login"] = None

if auth_status:
    st.title("Use Wook`s 🏖️Paradise")
    st. write("간단한 로그인 구현을 위한 노가다")
    st.session_state["auth_login"] = "로그인 중"
    st.sidebar.success("로그인 성공")
    auth.logout('logout','sidebar')
