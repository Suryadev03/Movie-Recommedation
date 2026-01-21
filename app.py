import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

st.title('Movie Recommendation System using Google Gemini API')
user_input = st.text_input('Enter a movie name:')
submit_button = st.button('Get Recommendations')

st.write('Movie name Entered:', user_input)

genai.configure(api_key=os.getenv('GOOGLE-GEMINI-API-KEY'))
model = genai.GenerativeModel('gemini-2.5-flash')

if submit_button:
    st.markdown("Fetching recommendations...")
    
    prompt = f"Recommend 5 movies based on the following movie name: {user_input}. Provide a brief description for each movie."
    response = model.generate_content(prompt)
    st.subheader('Movie Recommendations:')
    st.write(response.text) 
    

  

else:
    st.markdown("Please enter a movie name and click 'Get Recommendations'.")

