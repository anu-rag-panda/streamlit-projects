import streamlit as st
import pandas as pd
from data import Flight, FlightManager

def main():
    st.set_page_config(page_title="Flight Management Dashboard", layout="wide")
    st.title("✈️ Flight Management Dashboard")

    # Initialize session state
    if 'flight_manager' not in st.session_state:
        st.session_state.flight_manager = FlightManager()

    # Sidebar for adding flights
    with st.sidebar:
        st.header("Add New Flight")
        with st.form("new_flight", clear_on_submit=True):
            flight_number = st.text_input("Flight Number")
            source = st.text_input("Source")
            destination = st.text_input("Destination")
            fare = st.number_input("Fare", min_value=0.0)
            duration = st.number_input("Duration (hours)", min_value=0.0)
            
            if st.form_submit_button("Add Flight"):
                new_flight = Flight(flight_number, source, destination, fare, duration)
                st.session_state.flight_manager.add_flight(new_flight)
                st.success("Flight added successfully!")

    # Main content
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Flight List")
        df = st.session_state.flight_manager.to_dataframe()
        if not df.empty:
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No flights added yet")

    with col2:
        st.header("Filter Flights")
        max_fare = st.slider("Maximum Fare", 0.0, 50000.0, 1000.0)
        max_duration = st.slider("Maximum Duration (hours)", 0.0, 24.0, 5.0)
        
        if st.button("Filter"):
            filtered_flights = st.session_state.flight_manager.filter_flights(max_fare, max_duration)
            if filtered_flights:
                st.subheader("Filtered Results")
                filtered_df = pd.DataFrame([vars(f) for f in filtered_flights])
                st.dataframe(filtered_df)
            else:
                st.warning("No flights match the criteria")

if __name__ == "__main__":
    main()