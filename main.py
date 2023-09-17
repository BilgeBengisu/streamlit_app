import streamlit as st
import geonamescache
import openai

openai.api_key = ""


def run_conversation(city, country, time):
    # Step 1: send the conversation and available functions to GPT
    message_string = "Hello GPT! I'm going to %s, %s for %s day(s). Can you provide me a detailed travel plan day by day? Thank you!" % (
        city, country, time)
    messages = [{"role": "user", "content": message_string}]
    # functions = []
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages,
        # functions=functions,
        # function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    return response_message


st.set_page_config(page_title="Let's Travel!", page_icon="💃")
st.header('Welcome to the :blue[Travel Planner]', divider='rainbow')

# Generate list of countries and prompt user to select one.
gc = geonamescache.GeonamesCache()
countries = gc.get_countries()
country = st.selectbox('Which country are you going to?', map(
    lambda country: country['name'], countries.values()))

# Generate list of cities based on selected country and prompt user to select
# one.
cities = gc.search_cities(gc.get_countries_by_names()[
                          country]['iso'], attribute='countrycode')
city = st.selectbox('Which city are you going to?',
                    map(lambda city: city['name'], cities))

time = st.text_input("How many days will you be staying?")
travel_button = st.button("Let's Travel!")
if travel_button:
    st.write('Your travel to ', city, ", ", country, " for ", time, " day(s)")
    st.write(run_conversation(city, country, time))
