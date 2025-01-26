import streamlit as st
import pandas as pd
import numpy as np

# Set up page configuration
st.set_page_config(page_title="Simple Streamlit Dashboard", layout="wide")

# Sidebar for input
st.sidebar.header("User Input")
user_name = st.sidebar.text_input("Enter your name", "Guest")
user_age = st.sidebar.slider("Select your age", 18, 100, 25)

# Main area
st.title("Welcome to Your Personalized Dashboard!")
st.write(f"Hello, {user_name}!")
st.write(f"You are {user_age} years old.")

# Generating random data for plotting
data = pd.DataFrame({
    "Age": np.random.randint(20, 60, 100),
    "Score": np.random.randint(0, 100, 100)
})

# Button to generate plot
if st.sidebar.button("Generate Plot"):
    st.subheader("Age vs. Score")
    st.scatter_chart(data)

# Footer message
st.markdown("""
    --- 
    Created with ❤️ by Streamlit.
""")


