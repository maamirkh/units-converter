
import streamlit as st

def convert_units(value, unit_from, unit_to):

    conversions = {
        "meter_kilometer": 0.001, # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000, # 1 kilometer = 1000 meters
        "centimeter_meter": 0.01, # 1 centimeter = 0.01 meters
        "meter_centimeter": 100, # 1 meter = 100 centimeters
        "meter_feet": 3.28084, # 1 meter = 3.28084 feets
        "feet_meter": 0.3048, # 1 feet = 0.3048 meters
        "feet_yard": 0.333333, # 1 feet = 0.333333 yards
        "yard_feet": 3, # 1 yard = 3 feet
        "meter_yard": 1.09361, # 1 meter = 1.09361 yards
        "yards_meter": 0.9144, # 1 yard = 0.9144 meters
        "gram_kilogram": 0.001, # 1 gram = 0.001 kilogram
        "kilogram_gram": 1000, # 1 kilogram = 1000

    }

    key = f"{unit_from}_{unit_to}" # generate a key based on the input and output units

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "conversion not supported"
    
st.title("Unit Converter")

value = st.number_input("Enter the Value:")

unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "centimeter", "feet", "yard", "gram", "kilogram"])

unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "centimeter", "feet", "yard", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: {result}")