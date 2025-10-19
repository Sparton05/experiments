#import streamlit as st
#import requests

# Title
st.title("My First Streamlit App")

# Simple text
st.write("This app fetches data from the web!")

# Add a button
if st.button("Get Random Fact"):
    # Fetch data from a free API
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    data = response.json()
    st.success(data["text"])

# Input field
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! 👋")

# Display some data
st.subheader("Quick Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.write("---")
st.caption("Built with Streamlit")
