import streamlit as st

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100 # convert cm to (self, *args, **kwargs):
    bmi = weight / height_m ** 2
    return round(bmi, 2)

def get_bmi_catagory(bmi):
    if (bmi < 18.5):
        return "Underweight"
    elif (bmi >= 18.5 and bmi < 24.9):
        return "Normal weight"
    elif (bmi >= 25 and bmi < 19.9):
        return "Overweight"
    else:
        return "Obesity"
    
#streamlit UI
st.set_page_config(page_title="BMI Calculator", page_icon="🏋🏻", layout="centered")

st.title("BMI Calculator 🏋🏻")
st.write("Enter your weight and height to calculate your Body Mass Index (BMI).")

weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, step=1.0)
height = st.number_input("Height (cm)", min_value=50, max_value=250, step=1)

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        bmi_catagory = get_bmi_catagory(bmi)
        st.success(f"Your BMI is: {bmi} - {bmi_catagory}")
    else:
        st.error("Please enter valid weight and height values.")
else:
    st.info("Click the button to calculate your BMI.")
    
st.write("Made with ❤️ by Anurag Panda")
    
