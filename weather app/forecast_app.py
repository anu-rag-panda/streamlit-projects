import streamlit as st
import requests
from datetime import datetime

# Streamlit UI
st.set_page_config(page_title="Advanced Weather App", page_icon="⛅")
st.title("🌦️ Weather App with Forecast (WeatherAPI)")
st.write("Get current weather and 3-day forecast using WeatherAPI.com")

# Input
city = st.text_input("Enter a city")

# API config
api_key = "f3e8d53d620044529f665518250607"  # 🔁 Replace with your actual WeatherAPI key
forecast_url = "http://api.weatherapi.com/v1/forecast.json"

# Fetch weather data
if city:
    params = {
        "key": api_key,
        "q": city,
        "days": 3,
        "aqi": "no",
        "alerts": "no"
    }

    res = requests.get(forecast_url, params=params)

    if res.status_code == 200:
        data = res.json()

        # Current Weather
        location = data["location"]
        current = data["current"]
        forecast = data["forecast"]["forecastday"]

        st.subheader(f"📍 {location['name']}, {location['country']}")
        st.image("https:" + current["condition"]["icon"], width=80)
        st.write(f"**🌡️ Temperature:** {current['temp_c']}°C (Feels like {current['feelslike_c']}°C)")
        st.write(f"**☁️ Condition:** {current['condition']['text']}")
        st.write(f"**💧 Humidity:** {current['humidity']}%")
        st.write(f"**💨 Wind:** {current['wind_kph']} km/h")
        st.write(f"**🕒 Last Updated:** {current['last_updated']}")

        st.markdown("---")
        st.subheader("📅 3-Day Forecast")

        for day in forecast:
            date = datetime.strptime(day["date"], "%Y-%m-%d").strftime("%A, %d %B %Y")
            day_data = day["day"]
            astro = day["astro"]
            st.markdown(f"### 📆 {date}")
            st.image("https:" + day_data["condition"]["icon"], width=60)
            st.write(f"**🌡️ Avg Temp:** {day_data['avgtemp_c']}°C")
            st.write(f"**🌞 Max:** {day_data['maxtemp_c']}°C | **🌙 Min:** {day_data['mintemp_c']}°C")
            st.write(f"**☁️ Condition:** {day_data['condition']['text']}")
            st.write(f"**💧 Humidity:** {day_data['avghumidity']}%")
            st.write(f"**🌄 Sunrise:** {astro['sunrise']} | **🌇 Sunset:** {astro['sunset']}")
            st.markdown("---")

    else:
        st.error("⚠️ Failed to fetch weather data. Please check your API key or city name.")
