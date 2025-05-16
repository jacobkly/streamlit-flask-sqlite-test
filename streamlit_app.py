import streamlit as st
import requests

st.title("Simple Flask + Streamlit + SQLite App")

name = st.text_input("Enter your name")

if st.button("Add Name"):
    if name.strip():
        res = requests.post("http://localhost:5000/add", 
                           json={"name": name})
        if res.ok:
            st.success("Name successfully added!")
        else:
            st.error("Filed to add name.")

st.header("All names in DB")
res = requests.get("http://localhost:5000/users")
if res.ok:
    users = res.json()
    for i, user in enumerate(users, 1):
        st.write(f"{i}. {user}")