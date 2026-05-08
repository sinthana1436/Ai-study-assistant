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
answer = {"gravity":"gravity is an ","water":"needed for life"}
def answer_question(question):

    q = question.lower()

    for key in answers:

        if key in q:

            return answers[key]

    return "I don't know this answer yet."
question = st.text_input("ask yours doublt!")
if st.button("submit"):
   if question:
      answer = answer_question(question)

        st.success(answer)

   else:
        st.warning("Please enter a question.")
   
