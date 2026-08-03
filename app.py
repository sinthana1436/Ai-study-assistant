import streamlit as st
import google.generativeai as genai
import sqlite3
from datetime import date



genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")



connection = sqlite3.connect("study_app.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS study_plans(
id INTEGER PRIMARY KEY AUTOINCREMENT,
subject TEXT,
exam_date TEXT,
hours INTEGER,
weak_topic TEXT,
study_plan TEXT
)
""")

connection.commit()



def generate_ai_response(prompt):

    response = model.generate_content(prompt)

    return response.text


def save_study_plan(subject, exam_date, hours, weak_topic, study_plan):

    cursor.execute("""
    INSERT INTO study_plans
    (subject,exam_date,hours,weak_topic,study_plan)

    VALUES(?,?,?,?,?)
    """,

    (subject,
    exam_date,
    hours,
    weak_topic,
    study_plan))

    connection.commit()


def get_saved_plans():

    cursor.execute("SELECT * FROM study_plans")

    rows = cursor.fetchall()

    return rows



st.title("AI Study Mentor")

st.header("Create Your Study Plan")

subject = st.text_input("Subject")

exam_date = st.date_input("Exam Date")

hours = st.number_input(
"Study Hours Per Day",
min_value=1,
max_value=12
)

weak_topic = st.text_input("Weak Topic")

level = st.selectbox(

"Student Level",

[
"Beginner",
"Intermediate",
"Advanced"
]

)

mode = st.selectbox(

"Study Mode",

[
"Exam Preparation",
"Personalized Exam Coach"
]

)

uploaded_pdf = st.file_uploader(

"Upload PDF",

type=["pdf"]

)



if st.button("Generate Study Plan"):

    prompt = f"""
You are an expert study planner.

Subject:
{subject}

Exam Date:
{exam_date}

Study Hours:
{hours}

Weak Topic:
{weak_topic}

Student Level:
{level}

Mode:
{mode}

Create

1. Day Wise Plan

2. Revision Schedule

3. Daily Targets

4. Motivation

5. Tips
"""

    study_plan = generate_ai_response(prompt)

    st.subheader("Your Study Plan")

    st.write(study_plan)

    save_study_plan(

    subject,

    exam_date,

    hours,

    weak_topic,

    study_plan

    )



if st.button("Show Saved Plans"):

    plans = get_saved_plans()

    for row in plans:

        st.write(row)

connection.close()
