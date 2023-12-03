import pickle
from pathlib import Path

import streamlit_authenticator as sa

name = ["이용욱","김성은"]
username =["zealot","nanjangi"]
password = ["1234","4321"]

hashed_password = sa.Hasher(password).generate()
file_path = Path(__file__).parent / "hashed_pw.pkl"

with file_path.open("wb") as file:
    pickle.dump(hashed_password,file)