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
if st.button("submit"):
   if question:
      q=question.lower()
      if "gravity" in q:
         st.success("gravity is my world")
      elif "water" in q:
         st.success("water makes life")
      else:
         st.info("i dont't know the answer")
   else:
      st.warning(" enter somthing ")
st.divider()
topics=["gravity","AP","python"]
st.subheader("available topics")
for topic in topics:
   st.write(topic)

   
