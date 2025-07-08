import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(page_icon="🦠", page_title="COVID 19 Tracker", layout="centered")

st.title("COVID 19 Global and Country-wise Tracker")
st.write("Live Data Sourced From [covid19api.com](https://covid19api.com)")

#load list of countries
@st.cache_data
def load_countries():
    url = "https://api.covid19api.com/countries"
    res = requests.get(url).json()
    country = pd.DataFrame(res)
    countries = country.sort_values(by="Country")
    return countries

countries = load_countries()

country_list = countries["Country"].tolist()
country_list.insert(0, "Global")

# Select country
selected_country = st.selectbox("Select a Country", country_list)

# Fetch data based on selected country
@st.cache_data
def fetch_data(country):
    if country == "Global":
        url = "https://api.covid19api.com/summary"
        res = requests.get(url).json()
        data = res["Global"]
        df = pd.DataFrame([data])
        df["Date"] = pd.to_datetime(res["Date"])
        df["Country"] = "Global"
        return df
        
    else:
        url = f"https://api.covid19api.com/dayone/country/{country.lower()}"
        res = requests.get(url).json()
        df = pd.DataFrame(res)
        df = df[df["Status"] == "confirmed"]
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.groupby("Date").sum().reset_index()
        df["Country"] = country
        return df
    
data_fetched = fetch_data(selected_country)

# Display data
st.subheader(f"Data for {selected_country}")
if not data_fetched.empty:
    st.write(data_fetched)
    
    # Plotting
    fig = px.line(data_fetched, x="Date", y="Cases", title=f"COVID-19 Cases in {selected_country}")
    st.plotly_chart(fig)
    
else:
    st.error("No data available for the selected country.")
    
# Footer
st.markdown("---")
st.markdown("Made with ❤️ by [Anurag Panda](https://linkedin.com/in/anurag-panda-)")



