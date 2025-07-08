import streamlit as st
import requests
import time
import pandas as pd
import plotly.express as px

# ThingSpeak configuration (replace with your credentials)
CHANNEL_ID = "YOUR_CHANNEL_ID"
READ_API_KEY = "YOUR_READ_API_KEY"
WRITE_API_KEY = "YOUR_WRITE_API_KEY"

# Endpoints
DATA_URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=100"
CONTROL_URL = "https://api.thingspeak.com/update"

# Initialize session state
if 'device_states' not in st.session_state:
    st.session_state.device_states = {"light": 0, "fan": 0}

# Fetch data from ThingSpeak
def fetch_sensor_data():
    try:
        response = requests.get(DATA_URL)
        data = response.json()
        feeds = data.get('feeds', [])
        
        # Process data into DataFrame
        sensor_data = []
        for feed in feeds:
            if feed.get('field1') and feed.get('field2'):
                sensor_data.append({
                    'timestamp': feed['created_at'],
                    'temperature': float(feed['field1']),
                    'humidity': float(feed['field2'])
                })
        return pd.DataFrame(sensor_data)
    except:
        return pd.DataFrame()

# Update device state
def update_device(device, state):
    params = {
        'api_key': WRITE_API_KEY,
        f'field{3 if device=="light" else 4}': state
    }
    requests.post(CONTROL_URL, params=params)
    st.session_state.device_states[device] = state

# Dashboard layout
st.title("🌡️ IoT Dashboard with ThingSpeak")
st.subheader("Real-time Sensor Monitoring & Device Control")

# Fetch and display sensor data
df = fetch_sensor_data()
if not df.empty:
    # Latest readings
    latest = df.iloc[-1]
    col1, col2 = st.columns(2)
    col1.metric("Temperature", f"{latest['temperature']}°C")
    col2.metric("Humidity", f"{latest['humidity']}%")
    
    # Historical charts
    tab1, tab2 = st.tabs(["Temperature Trend", "Humidity Trend"])
    with tab1:
        fig = px.line(df, x='timestamp', y='temperature', title="Temperature History")
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        fig = px.line(df, x='timestamp', y='humidity', title="Humidity History")
        st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No sensor data available. Check your ThingSpeak configuration.")

# Device control section
st.subheader("⚙️ Device Control")
col1, col2 = st.columns(2)

# Light control
with col1:
    st.write("**Light Control**")
    light_state = st.session_state.device_states["light"]
    if st.button("💡 TURN ON" if light_state == 0 else "🔌 TURN OFF", 
                 key="light_btn", 
                 type="primary" if light_state == 0 else "secondary"):
        update_device("light", 0 if light_state == 1 else 1)

# Fan control
with col2:
    st.write("**Fan Control**")
    fan_state = st.session_state.device_states["fan"]
    if st.button("🌀 TURN ON" if fan_state == 0 else "🔌 TURN OFF", 
                 key="fan_btn", 
                 type="primary" if fan_state == 0 else "secondary"):
        update_device("fan", 0 if fan_state == 1 else 1)

# Status indicators
st.write("**Device Status**")
status_cols = st.columns(2)
status_cols[0].write(f"Light: {'🟢 ON' if st.session_state.device_states['light'] else '🔴 OFF'}")
status_cols[1].write(f"Fan: {'🟢 ON' if st.session_state.device_states['fan'] else '🔴 OFF'}")

# Auto-refresh
st.caption("Data refreshes every 10 seconds")
time.sleep(10)
st.rerun()
