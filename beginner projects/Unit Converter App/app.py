import streamlit as st

# Base unit: metric or logical base for each type
length_units = {
    "Meter": 1,
    "Kilometer": 1000,
    "Centimeter": 0.01,
    "Millimeter": 0.001,
    "Mile": 1609.34,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254,
}

weight_units = {
    "Kilogram": 1,
    "Gram": 0.001,
    "Pound": 0.453592,
    "Ounce": 0.0283495,
    "Ton": 1000,
}

temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

currency_rates = {
    "USD": 1.0,
    "INR": 83.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 157.0,
}

time_units = {
    "Second": 1,
    "Minute": 60,
    "Hour": 3600,
    "Day": 86400,
}

speed_units = {
    "m/s": 1,
    "km/h": 1/3.6,
    "mph": 0.44704,
    "knot": 0.514444,
    "ft/s": 0.3048,
}

area_units = {
    "Square Meter": 1,
    "Square Kilometer": 1e6,
    "Square Centimeter": 0.0001,
    "Square Millimeter": 0.000001,
    "Square Mile": 2.59e6,
    "Square Yard": 0.836127,
    "Square Foot": 0.092903,
    "Square Inch": 0.00064516,
    "Acre": 4046.86,
    "Hectare": 10000,
}

volume_units = {
    "Cubic Meter": 1,
    "Liter": 0.001,
    "Milliliter": 0.000001,
    "Cubic Centimeter": 0.000001,
    "Cubic Millimeter": 1e-9,
    "Cubic Foot": 0.0283168,
    "Cubic Inch": 0.0000163871,
    "Gallon (US)": 0.00378541,
    "Pint (US)": 0.000473176,
}

# Function for temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Fahrenheit":
        c = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        c = value - 273.15
    else:
        c = value

    if to_unit == "Fahrenheit":
        return c * 9 / 5 + 32
    elif to_unit == "Kelvin":
        return c + 273.15
    else:
        return c

# UI
st.set_page_config(page_title="Universal Unit Converter", layout="centered")
st.title("🌍 Universal Unit Converter")

unit_type = st.selectbox("Select Unit Type", [
    "Length", "Weight", "Temperature", "Currency", "Time", "Speed", "Area", "Volume"
])

def convert_units(value, from_unit, to_unit, unit_dict):
    base = value * unit_dict[from_unit]
    return base / unit_dict[to_unit]

# Logic
if unit_type == "Temperature":
    from_unit = st.selectbox("From", temperature_units)
    to_unit = st.selectbox("To", temperature_units)
    value = st.number_input("Enter Temperature", format="%.2f")

    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")

elif unit_type == "Currency":
    units = list(currency_rates.keys())
    from_unit = st.selectbox("From Currency", units)
    to_unit = st.selectbox("To Currency", units)
    value = st.number_input("Enter Amount", format="%.2f")

    if st.button("Convert"):
        base = value / currency_rates[from_unit]
        result = base * currency_rates[to_unit]
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

else:
    if unit_type == "Length":
        unit_dict = length_units
    elif unit_type == "Weight":
        unit_dict = weight_units
    elif unit_type == "Time":
        unit_dict = time_units
    elif unit_type == "Speed":
        unit_dict = speed_units
    elif unit_type == "Area":
        unit_dict = area_units
    elif unit_type == "Volume":
        unit_dict = volume_units
    else:
        unit_dict = {}

    units = list(unit_dict.keys())
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter Value", format="%.4f")

    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, unit_dict)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

st.write("Made with ❤️ by Anurag Panda")
