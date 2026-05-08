import streamlit as st
import requests

st.title("Studyz")
st.write("your ai mentor")
name = st.text_input("what is your good name")
if st.button("click"):
   if name:
      st.success(f"hi {name}♡ welcome to studyz")
   else:
         st.warning("please give your name")
st.divider()
def answer_question(question):
   api_key=
   URL =
   headers ={"authorisation":f"bearer{api_key}"}
   data={"questions":question}
   response=requests.post(URL,headers=headers,json=data)
   result=response.json()
   try:
      return result["answer"]
   except:
      return "i don't know"

    
question = st.text_input("ask yours doublt!")
if st.button("submit"):
   if question:
      answer = answer_question(question)

      st.success(answer)

   else:
      st.warning("Please enter a question.")
   
