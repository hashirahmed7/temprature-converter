import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

# Function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Streamlit interface setup
st.title("Temperature Converter")
st.markdown("""
    Welcome to the **Temperature Converter** app! Convert between Celsius, Fahrenheit, and Kelvin.
    Choose the temperature scale you want to convert from and to.
""")
st.image("https://images.unsplash.com/photo-1593642532973-d31b6557fa68", use_column_width=True)

# User input for temperature value
temperature_value = st.number_input("Enter temperature value:", -273.15, 10000.0, 0.0)

# Dropdown for selecting the scale to convert from
from_scale = st.selectbox("Convert from:", ["Celsius", "Fahrenheit", "Kelvin"])

# Dropdown for selecting the scale to convert to
to_scale = st.selectbox("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])

# Perform conversion based on selected options
if from_scale == "Celsius":
    if to_scale == "Fahrenheit":
        result = celsius_to_fahrenheit(temperature_value)
    elif to_scale == "Kelvin":
        result = celsius_to_kelvin(temperature_value)
    else:
        result = temperature_value

elif from_scale == "Fahrenheit":
    if to_scale == "Celsius":
        result = fahrenheit_to_celsius(temperature_value)
    elif to_scale == "Kelvin":
        result = fahrenheit_to_kelvin(temperature_value)
    else:
        result = temperature_value

elif from_scale == "Kelvin":
    if to_scale == "Celsius":
        result = kelvin_to_celsius(temperature_value)
    elif to_scale == "Fahrenheit":
        result = kelvin_to_fahrenheit(temperature_value)
    else:
        result = temperature_value

# Display the result
st.subheader(f"Converted Temperature: {result:.2f} {to_scale}")

# Styling and layout adjustments
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f0f5;
        padding: 20px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 5px;
    }
    .stSelectbox select {
        font-size: 16px;
    }
    .stNumberInput input {
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)
