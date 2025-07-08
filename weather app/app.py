import streamlit as st
import requests
from datetime import datetime

#app title
st.set_page_config(page_title="Weather App", page_icon=":cloud:", layout="wide")
st.title("Weather App :cloud:")
st.write("Enter a city name to get the current weather information.")

#input field
city = st.text_input("City Name", placeholder="Enter city name...")

#api key
API_KEY = "your api key here"

#fetch weather data
if city:
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": "f3e8d53d620044529f665518250607",
        "q": city,
        "aqi": "no"
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        location = data['location']['name']
        country = data['location']['country']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        icon_url = "https:" + data['current']['condition']['icon']
        wind_kph = data['current']['wind_kph']
        humidity = data['current']['humidity']
        feels_like = data['current']['feelslike_c']

        st.subheader(f"📍 Weather in {location}, {country}")
        st.image(icon_url, width=80)
        st.write(f"**🌡️ Temperature:** {temp_c}°C (Feels like {feels_like}°C)")
        st.write(f"**☁️ Condition:** {condition}")
        st.write(f"**💧 Humidity:** {humidity}%")
        st.write(f"**💨 Wind Speed:** {wind_kph} km/h")
    else:
        st.error("City not found. Please check the name and try again.")
        
#footer
st.markdown("---")
st.markdown("Made with ❤️ by Anurag Panda")




