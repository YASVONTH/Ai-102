import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AQ.Ab8RN6JIGyWtoqsuqTMbxUir06E2zn3HN_QgA3iR4xnCKT6HFw")
model=genai.GenerativeModel("gemini-2.5-flash")
qns=st.text_input("Enter the question:")
if st.button("submit"):
    res=model.generate_content(qns+"you want to explain the code of the given code.")
    st.write(res.text)