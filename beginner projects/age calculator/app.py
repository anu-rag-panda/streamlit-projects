import streamlit as st
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="Age Calculator", layout="centered")
st.title("🎂 Age Calculator")

st.write("Select your date of birth to calculate your exact age:")

# Input: Date of Birth
dob = st.date_input("Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())

# Output: Age
if st.button("Calculate Age"):
    today = date.today()

    if dob > today:
        st.error("Date of Birth cannot be in the future.")
    else:
        delta = relativedelta(today, dob)

        years = delta.years
        months = delta.months
        days = delta.days

        st.success(f"🎉 You are {years} years, {months} months, and {days} days old!")

        # Optional extras
        total_days = (today - dob).days
        next_birthday = dob.replace(year=today.year if dob.replace(year=today.year) >= today else today.year + 1)
        days_to_birthday = (next_birthday - today).days

        st.info(f"🗓 Total Days Alive: {total_days} days")
        st.info(f"🎁 Days Until Next Birthday: {days_to_birthday} days")
