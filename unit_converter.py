import streamlit as st

# Set page configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Define Conversion Functions
def convert_length(val, from_unit, to_unit):
    conversion_factors = {
        "Kilometer": 1e3,
        "Meter": 1,
        "Centimeter": 1e-2,
        "Millimeter": 1e-3,
        "Micrometer": 1e-6,
        "Nanometer": 1e-9,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Nautical Mile": 1852
    }
    return val * (conversion_factors[from_unit] / conversion_factors[to_unit]) if from_unit in conversion_factors and to_unit in conversion_factors else val

def convert_weight(val, from_unit, to_unit):
    conversion_factors = {
        "Kilograms": 1,
        "Pounds": 2.20462,
        "Gram": 1000,
        "Microgram": 1e6
    }
    return val * (conversion_factors[to_unit] / conversion_factors[from_unit]) if from_unit in conversion_factors and to_unit in conversion_factors else val

def convert_temp(val, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (val * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (val - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return val + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return val - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (val - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (val - 273.15) * 9/5 + 32
    return val

# App Title
st.title("🔄 Unit Converter")

# Conversion Category
category = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

# Length Conversion Units
length_units = [
    "Kilometer", "Meter", "Centimeter", "Millimeter", "Micrometer", "Nanometer", 
    "Mile", "Yard", "Foot", "Inch", "Nautical Mile"
]
weight_units = ["Kilograms", "Pounds", "Gram", "Microgram"]
temp_units = ["Celsius", "Fahrenheit", "Kelvin"]

if category == "Length":
    available_units = length_units
elif category == "Weight":
    available_units = weight_units
else:
    available_units = temp_units

# Single Conversion
col1, col2 = st.columns(2)
with col1:
    unit_from = st.selectbox("From", available_units)
with col2:
    unit_to = st.selectbox("To", available_units)

value = st.number_input("Enter Value", format="%.2f") if category == "Temperature" else st.number_input("Enter Value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    if category == "Length":
        result = convert_length(value, unit_from, unit_to)
    elif category == "Weight":
        result = convert_weight(value, unit_from, unit_to)
    else:
        result = convert_temp(value, unit_from, unit_to)

    st.success(f"Converted Value: {result:.6f} {unit_to}")

# Footer
st.markdown("---")
st.markdown("🚀 **Created by Muhammad Bilal Hussain** | Powered by **Streamlit**")
st.markdown("""
    <div style='text-align: center; font-size: 18px; font-weight: bold;'>
        <a href='https://www.linkedin.com/in/bilalcode01/' target='_blank' style='margin-right: 20px; text-decoration: none; color: #0077b5;'>🔗 LinkedIn</a>
        <a href='https://github.com/Bilal0335' target='_blank' style='text-decoration: none; color: #333;'>🐙 GitHub</a>
    </div>
""", unsafe_allow_html=True)
