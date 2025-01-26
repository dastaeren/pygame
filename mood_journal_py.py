import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Input field
user_input = st.text_input("Enter some text:")

# Display the entered text
if user_input:
    st.write(f"You entered: {user_input}")
else:
    st.write("No text entered yet.")

