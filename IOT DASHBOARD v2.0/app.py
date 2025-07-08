import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import time

st.set_page_config(page_title="IoT Dashboard", layout="wide")

st.title("📊 IoT Dashboard with ThingSpeak")

# Sidebar inputs
st.sidebar.header("🔧 Configuration")
channel_id = st.sidebar.text_input("ThingSpeak Channel ID", "YOUR_CHANNEL_ID")
read_api_key = st.sidebar.text_input("Read API Key (Optional)", "")
num_results = st.sidebar.slider("Number of Entries to Show", 10, 100, 50)
refresh_rate = st.sidebar.slider("Auto Refresh (seconds)", 0, 300, 0)

def get_data():
    # Get channel info first
    channel_url = f"https://api.thingspeak.com/channels/{channel_id}.json"
    if read_api_key:
        channel_url += f"?api_key={read_api_key}"
    
    channel_response = requests.get(channel_url)
    field_names = {}
    
    if channel_response.status_code == 200:
        channel_data = channel_response.json()
        # Extract field names
        for i in range(1, 11):
            field_key = f'field{i}'
            if channel_data.get(field_key):
                field_names[field_key] = channel_data[field_key]
    
    # Get feed data
    url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?results={num_results}"
    if read_api_key:
        url += f"&api_key={read_api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['feeds'])
        df['created_at'] = pd.to_datetime(df['created_at'])
        df = df.set_index('created_at')
        return df, field_names
    else:
        st.error("Failed to fetch data. Check Channel ID/API Key.")
        return None, None
    


placeholder = st.empty()

while True:
    df, field_names = get_data()
    if df is not None:
        with placeholder.container():
            st.subheader("📍 Latest Field Values")
            cols = st.columns(5)
            for i in range(1, 11):
                field = f'field{i}'
                if field in df.columns:
                    field_label = field_names.get(field, f"Field {i}")
                    value = df[field].dropna().iloc[-1] if not df[field].dropna().empty else "N/A"
                    cols[(i-1)%5].metric(field_label, value)

            st.markdown("---")
            st.subheader("📈 Field Graphs")
            for i in range(1, 11):
                field = f'field{i}'
                if field in df.columns:
                    field_label = field_names.get(field, f"Field {i}")
                    fig = px.line(df, y=field, title=f"{field_label} Graph", labels={field: field_label, "created_at": "Time"})
                    st.plotly_chart(fig, use_container_width=True, key=f"plot_{field}")  # Added unique key
    if refresh_rate == 0:
        break
    else:
        time.sleep(refresh_rate)
