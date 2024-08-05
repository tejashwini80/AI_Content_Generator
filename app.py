import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import os



# Load environment variables
load_dotenv()

# Configure the API key from environment variables
genai.configure(api_key=os.environ["API_KEY"])

# Set the title of the web app
# Title of the app
st.title("AI Content Generation")
 

# Create a text input box for user input
user_input = st.text_area("Enter your input here!", height=20)

if 'generated_content' not in st.session_state:
    st.session_state.generated_content = ""

# Function to generate content based on a given prompt
def generate_content(prompt):
    

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(
        [prompt],
        safety_settings={
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE},
    )
    return response.text


col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Generate A Story"):
        if user_input:
            generated_content = generate_content(f"Generate a narrative  story  tailored for {user_input}, including a list of necessary characters, and their description.")
            st.session_state.generated_content = ""
            st.session_state.generated_content += generated_content

with col2:
    if st.button("Generate Shayari"):
        if user_input:
            generated_content = generate_content(f"Compose an evocative Poetry in English that beautifully captures the essence of {user_input}, blending emotion and imagery to convey deep feelings.")
            st.session_state.generated_content = ""
            st.session_state.generated_content += generated_content

with col3:
    if st.button("Covert to Quote"):
        if user_input:
            generated_content = generate_content(f"Translate the following into a meaningful and a thought-provoking quote t: {user_input}")
            st.session_state.generated_content = ""
            st.session_state.generated_content += generated_content

with col4:
    if st.button("Generate a Joke"):
        if user_input:
            generated_content = generate_content(f"Craft a hilarious joke mimicing the  scenario described: {user_input}. Ensure the message is clear, well-structured, and appropriate for the context provided.")
            st.session_state.generated_content = ""
            st.session_state.generated_content += generated_content

st.text_area("Generated Content", st.session_state.generated_content, height=500)