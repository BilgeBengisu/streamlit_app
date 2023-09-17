
import streamlit as st


st.set_page_config(page_title="Let's Travel!", page_icon="💃")
st.header('Welcome to the :blue[Travel Planner]', divider='rainbow')

country = st.text_input('Which country are you going to?')
city = st.text_input('Which city are you going to?')
time = st.text_input("How long will you be there?")
travel_button = st.button("Let's Travel!")

st.write('Your travel to ', city, ", ", country, " for ", time, "day(s)")
