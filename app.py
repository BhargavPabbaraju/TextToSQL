from dotenv import load_dotenv

load_dotenv()

import google.generativeai as genai

import streamlit as st
import os
import sqlite3



#Configure our api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Load google gemini model
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

# Retrieve query from sql database
def read_sql_query(sql,db,verbose=False):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    if verbose:
        for row in rows:
            print(row)

    return rows

prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name pokemon and has the following columns - id, name, 
    type1, type2,  atk, def, spatk, spdef, speed \n\nFor example,\n
    Example 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM pokemon ;
    \nExample 2 - Tell me all the pokemon which are fire type?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where type1="Fire" OR type2="Fire"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    
    """
]

#Streamlit App
st.set_page_config(page_title="I can retrieve Any SQL query")
st.header("Gemini App to Retrieve SQL Data")
question = st.text_input("Input: ",key="input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data = read_sql_query(response,"student.db")
    st.subheader("The Response is ")
    for row in data:
        print(row)
        st.header(row)