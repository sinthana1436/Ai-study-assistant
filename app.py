import streamlit as st

st.title("Studyz")
st.write("your ai mentor")
name = st.text_input("what is your good name")
if st.button("click"):
   if name:
      st.success(f"hi{name}♡ welcome to studyz")
   else:
         st.warning("please give your name")
st.divider()
question = st.text_input("ask yours doublt!")
if question:
   st.write("you asked:",question)
   st.info("your ai mentor in on his way")

   
