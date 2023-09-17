import streamlit as st
import openai

openai.api_key = openai_key
def run_conversation(city, country, time):
    # Step 1: send the conversation and available functions to GPT
    message_string = "Hello GPT! I'm going to %s, %s for %s day(s). Can you provide me a detailed travel plan day by day? Thank you!" % (city, country, time)
    messages = [{"role": "user", "content": message_string}]
    #functions = []
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages,
        #functions=functions,
        #function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    return response_message

st.set_page_config(page_title="Let's Travel!", page_icon="💃")
st.header('Welcome to the :blue[Travel Planner]', divider='rainbow')

country = st.text_input('Which country are you going to?')
city = st.text_input('Which city are you going to?')
time = st.text_input("How long will you be there?")
travel_button = st.button("Let's Travel!")
if travel_button:
    st.write('Your travel to ', city, ", ", country, " for ", time, " day(s)", model=True)
    st.write(run_conversation(city, country, time))






