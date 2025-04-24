import streamlit as st

def main():
    st.title("Unit Converter")
    
    # Initialize session state for conversion history
    if 'conversion_history' not in st.session_state:
        st.session_state.conversion_history = []
    
    # Create a sidebar for category selection
    category = st.sidebar.selectbox(
        "Select Conversion Category",
        ["Length", "Weight", "Temperature"]
    )
    
    # Main conversion logic
    if category == "Length":
        st.header("Length Conversion")
        input_value = st.number_input("Enter value:", value=0.0)
        from_unit = st.selectbox("From:", ["Meters", "Kilometers", "Miles", "Feet", "Inches"])
        to_unit = st.selectbox("To:", ["Meters", "Kilometers", "Miles", "Feet", "Inches"])
        
        # Conversion factors (to meters as base unit)
        length_factors = {
            "Meters": 1,
            "Kilometers": 1000,
            "Miles": 1609.34,
            "Feet": 0.3048,
            "Inches": 0.0254
        }
        
        # Convert to base unit (meters) then to target unit
        result = input_value * length_factors[from_unit] / length_factors[to_unit]
        st.success(f"{input_value} {from_unit} = {result:.4f} {to_unit}")
        
        # Add to history
        st.session_state.conversion_history.append(
            f"{input_value} {from_unit} = {result:.4f} {to_unit}"
        )
        
    elif category == "Weight":
        st.header("Weight Conversion")
        input_value = st.number_input("Enter value:", value=0.0)
        from_unit = st.selectbox("From:", ["Kilograms", "Grams", "Pounds", "Ounces"])
        to_unit = st.selectbox("To:", ["Kilograms", "Grams", "Pounds", "Ounces"])
        
        # Conversion factors (to kilograms as base unit)
        weight_factors = {
            "Kilograms": 1,
            "Grams": 0.001,
            "Pounds": 0.453592,
            "Ounces": 0.0283495
        }
        
        # Convert to base unit (kilograms) then to target unit
        result = input_value * weight_factors[from_unit] / weight_factors[to_unit]
        st.success(f"{input_value} {from_unit} = {result:.4f} {to_unit}")
        
        # Add to history
        st.session_state.conversion_history.append(
            f"{input_value} {from_unit} = {result:.4f} {to_unit}"
        )
        
    elif category == "Temperature":
        st.header("Temperature Conversion")
        input_value = st.number_input("Enter value:", value=0.0)
        from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])
        
        # Temperature conversion requires special formulas
        def convert_temperature(value, from_unit, to_unit):
            # First convert to Celsius as base unit
            if from_unit == "Fahrenheit":
                celsius = (value - 32) * 5/9
            elif from_unit == "Kelvin":
                celsius = value - 273.15
            else:
                celsius = value
                
            # Then convert to target unit
            if to_unit == "Fahrenheit":
                return (celsius * 9/5) + 32
            elif to_unit == "Kelvin":
                return celsius + 273.15
            else:
                return celsius
        
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} = {result:.4f} {to_unit}")
        
        # Add to history
        st.session_state.conversion_history.append(
            f"{input_value} {from_unit} = {result:.4f} {to_unit}"
        )
    
    # Display conversion history
    if st.session_state.conversion_history:
        st.header("Conversion History")
        for conversion in reversed(st.session_state.conversion_history[-5:]):  # Show last 5 conversions
            st.text(conversion)
        
        # Add clear history button
        if st.button("Clear History"):
            st.session_state.conversion_history = []
            st.experimental_rerun()

if __name__ == "__main__":
    main()
