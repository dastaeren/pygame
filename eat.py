import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import datetime

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Create a placeholder for user input
st.title("MindEase AI - Mood Journal")
st.write("Track your feelings and get personalized well-being tips.")

# Input field for daily mood journal
journal_entry = st.text_area("Write today's journal entry:", "")

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment = analyzer.polarity_scores(text)
    return sentiment['compound']  # Compound score: -1 (negative) to +1 (positive)

# Initialize an empty DataFrame if there's no saved data
if 'mood_data' not in st.session_state:
    st.session_state['mood_data'] = pd.DataFrame(columns=["Date", "Entry", "Sentiment"])

# Button to save the journal entry and analyze sentiment
if st.button("Save Entry"):
    if journal_entry:
        sentiment_score = analyze_sentiment(journal_entry)
        new_entry = {"Date": datetime.datetime.now(), "Entry": journal_entry, "Sentiment": sentiment_score}
        st.session_state['mood_data'] = st.session_state['mood_data'].append(new_entry, ignore_index=True)
        st.success("Your journal entry has been saved!")
    else:
        st.warning("Please write something to log your mood.")

# Show a simple chart of mood over time
if not st.session_state['mood_data'].empty:
    st.subheader("Mood Trends Over Time")

    # Plotting sentiment trends
    st.session_state['mood_data']['Date'] = pd.to_datetime(st.session_state['mood_data']['Date'])
    st.session_state['mood_data'].set_index('Date', inplace=True)
    st.session_state['mood_data'].resample('D').mean()['Sentiment'].plot(kind='line', figsize=(10, 6))

    plt.title('Mood Trends')
    plt.xlabel('Date')
    plt.ylabel('Sentiment Score')
    st.pyplot()

    # Display mood analysis
    avg_sentiment = st.session_state['mood_data']['Sentiment'].mean()
    if avg_sentiment > 0.1:
        st.write("You're doing well! Keep up the positive vibes.")
    elif avg_sentiment < -0.1:
        st.write("You might be feeling down. Take care of yourself, and consider talking to someone.")
    else:
        st.write("Your mood is neutral. Keep tracking and stay mindful!")

# Tips for well-being
st.subheader("Personalized Tips")
st.write("Based on your journal entries, here are some tips to help you feel better:")

if avg_sentiment < 0.0:
    st.write("- Try some breathing exercises to calm your mind.")
    st.write("- It may help to take a short walk or talk to a friend.")
elif avg_sentiment > 0.0:
    st.write("- Keep focusing on positive activities!")
    st.write("- Gratitude exercises can further boost your mood.")
else:
    st.write("- Consistency is key! Keep journaling to reflect on your feelings.")



