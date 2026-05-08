import streamlit as st

st.title("Studyz")
st.write("your ai mentor")
name = st.text_input("what is your good name")
if st.button("click"):
   if name:
      st.success(f"hi{name}♡ welcome to studyz")
   else:
         st.warning("please give your name")
   
