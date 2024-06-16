# Llama-3 Chat Application

## Overview
This is a simple web-based chat application powered by the Llama-3 language model from Hugging Face. It allows users to have conversational interactions with the model in a user-friendly interface.

## Features
- Users can input text messages in the chat interface.
- The Llama-3 model generates responses based on the user input.
- The chat history is displayed in the interface, showing both user input and model responses.

## Getting Started
To run the application locally, follow these steps:
1. Clone this GitHub repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory of the project.
4. Add your Hugging Face API token to the `.env` file in the format `API_TOKEN=your_api_token`.
5. Run the Streamlit app using `streamlit run llama_chat.py`.
6. Interact with the chat interface by entering text messages and clicking the "Send" button.

## Dependencies
- Streamlit: For building the web interface.
- Requests: For making HTTP requests to the Hugging Face API.
- Python-dotenv: For loading environment variables from a `.env` file.


## Project Link
[https://llama3-webapp.streamlit.app/](#)
