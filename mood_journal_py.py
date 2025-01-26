import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Mood-based Tips", layout="centered")

# Sidebar for input
st.sidebar.header("What's your mood today?")
mood = st.sidebar.radio("Select your current mood", ["Happy", "Sad", "Neutral"])

# Main area
st.title("Personalized Mood-based Tips")

# Function to provide tips based on mood
def get_mood_tip(mood):
    if mood == "Happy":
        return "That's great! Keep enjoying the positive vibes 😊. You might want to share your happiness with others!"
    elif mood == "Sad":
        return "I'm sorry you're feeling this way 😔. Take a few deep breaths and try to do something kind for yourself. Maybe listen to your favorite music or take a walk in nature. You deserve it!"
    elif mood == "Neutral":
        return "You're in a balanced mood. A great time to focus on productivity and self-care. Try tackling something small on your to-do list today!"

# Display mood tip
st.write(get_mood_tip(mood))

# Footer message
st.markdown("""
    --- 
    Take care of yourself! ❤️
""")



