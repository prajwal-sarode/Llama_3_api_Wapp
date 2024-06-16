import streamlit as st
import requests

# Replace with your actual Hugging Face Inference Endpoint URL and token
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"  # Update with actual endpoint
API_TOKEN = "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"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def generate_response(user_input):
    payload = {"inputs": user_input}
    response = query(payload)
    if 'error' in response:
        return response['error']
    else:
        return response[0]['generated_text']

# Streamlit web interface
st.title("Llama-3 Chat")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

if st.button("Send"):
    if user_input:
        response = generate_response(user_input)
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("llama", response))

# Display chat history with custom colors
for speaker, chat in st.session_state.chat_history:
    if speaker == "user":
        st.markdown(f"<div style='color: blue;'>You: {chat}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='color: green;'>Llama-3: {chat}</div>", unsafe_allow_html=True)
