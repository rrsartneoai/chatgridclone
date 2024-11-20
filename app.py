import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd

st.title("Smart Grid Chatbot")

# Placeholder for chatbot integration
st.header("Chatbot")
user_input = st.text_input("Ask a question about the smart grid:")
if user_input:
    response = chatbot.get_response(user_input)
    st.write(response)

# Data Visualization
st.header("Interactive Map")
grid_data = pd.read_csv("data.csv", nrows=4)
plant_data = pd.read_csv("data.csv", skiprows=5)

m = folium.Map(location=[40, -100], zoom_start=4)

for index, row in grid_data.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=row["name"],
    ).add_to(m)

for index, row in plant_data.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=row["name"],
        icon=folium.Icon(color="red"),
    ).add_to(m)

folium_static(m)
