import streamlit as st
import random
import time
# from openai import OpenAI
import os
from clarifai.client.model import Model
from dotenv import load_dotenv
load_dotenv()


clarifai_pat = os.getenv('CLARIFAI_PAT')
inference_params = dict(temperature=0.7, max_tokens=200, top_k = 50, top_p= 0.95)

st.title("Chatbot with Mistral /mixtral-8x7B-Instruct-v0_1")
# model_prediction = "test"
# prompt = "test"
# prediction = Model("https://clarifai.com/mistralai/completion/models/mixtral-8x7B-Instruct-v0_1").predict_by_bytes(prompt.encode(), input_type="text", inference_params=inference_params)
# st.write(prompt)
# st.write(prediction)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.chat_message("assistant"):
    st.write("Hello 👋, how can I help you?")


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        prompt =  "<s> [INST] " + prompt +  " [/INST]"
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

with st.chat_message("assistant"):
    message_placeholder = st.empty()
    # prompt = "<s> [INST]" + "translate bonjour in spanish" +  "[/INST]"
    model_prediction = Model("https://clarifai.com/mistralai/completion/models/mixtral-8x7B-Instruct-v0_1").predict_by_bytes(prompt.encode(), input_type="text", inference_params=inference_params)
    full_response = model_prediction.outputs[0].data.text.raw
    time.sleep(0.05)
    # Add a blinking cursor to simulate typing
    message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": full_response})