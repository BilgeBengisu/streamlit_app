import streamlit as st
import geonamescache

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

time = st.text_input("How long will you be there (days)?")
travel_button = st.button("Let's Travel!")
st.write('Your travel to ', city, ", ", country, " for ", time, "day(s)")
