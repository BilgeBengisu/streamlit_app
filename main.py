import streamlit as st
import geonamescache
import openai

openai.api_key = ""


def run_conversation(city, country, time):
    # Step 1: send the conversation and available functions to GPT
    message_string = "Hello GPT! I'm going to %s, %s for %s day(s). Can you provide me a detailed travel plan day by day? Thank you!" % (
        city, country, time)
    messages = [{"role": "user", "content": message_string}]
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages,
    )
    response_message = response["choices"][0]["message"]["content"]
    return response_message


def main():
    st.set_page_config(page_title="Let's Travel!", page_icon="💃")
    st.header('Welcome to the :blue[Travel Planner]', divider='rainbow')

    gc = geonamescache.GeonamesCache()
    # Display countries by name and remember the chosen country name and iso code
    countries = gc.get_countries()
    country = st.selectbox('Which country are you going to?', map(
        lambda country: country['name'], countries.values()))
    country_iso = gc.get_countries_by_names()[country]['iso']

    # Display cities in selected country and remember the chosen city name
    cities = gc.search_cities(country_iso, attribute='countrycode')
    city = st.selectbox('Which city are you going to?',
                        map(lambda city: city['name'], cities))
    city_details = gc.search_cities(city, 'name')[0]

    time = st.text_input("How many days will you be staying?")

    travel_button = st.button("Let's Travel!")

    if travel_button:
        st.write('Your travel to ', city, ", ",
                 country, " for ", time, " day(s)")
        # Extract lat and lon coords to generate a map centered on the chosen city.
        st.map(city_details)
        # Notify user that this slow action is actually happening
        with st.spinner(text="Building your itinerary..."):
            st.write(run_conversation(city, country, time))


if __name__ == "__main__":
    main()
