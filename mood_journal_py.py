pip install streamlit vaderSentiment matplotlib pandas numpy

import streamlit as st
import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Initialize Sentiment Intensity Analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)
    return score['compound']

# Function to save entries and analyze them
def save_entry(entry, date, sentiment_score):
    # Check if the file exists, if not, create an empty dataframe
    if os.path.exists("mood_data.csv"):
        data = pd.read_csv("mood_data.csv")
    else:
        data = pd.DataFrame(columns=["Date", "Entry", "Sentiment"])

    # Create a new entry and append it to the dataframe
    new_data = pd.DataFrame({"Date": [date], "Entry": [entry], "Sentiment": [sentiment_score]})
    data = pd.concat([data, new_data], ignore_index=True)

    # Save the updated dataframe to a CSV file
    data.to_csv("mood_data.csv", index=False)
    return data

# Plot mood trends
def plot_mood_trends(data):
    # Convert 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'])

    # Set 'Date' as index
    data.set_index('Date', inplace=True)

    # Plot rolling average of sentiment scores over a 7-day window
    data['Sentiment'].rolling(window=7).mean().plot(title="Mood Trends Over Time", figsize=(10,6))
    plt.xlabel("Date")
    plt.ylabel("Mood Score (Sentiment)")
    st.pyplot()

# Streamlit UI components
st.title("MindEase AI - Mood Journal")

# User input
entry = st.text_area("Write about your day:", "")
submit = st.button("Submit Entry")

if submit and entry:
    sentiment_score = analyze_sentiment(entry)
    date = datetime.now().strftime("%Y-%m-%d")
    data = save_entry(entry, date, sentiment_score)
    st.success("Your entry has been saved!")

    # Display sentiment score and recent entries
    st.write(f"Sentiment Score: {sentiment_score}")
    st.write("Recent Entries:")
    st.dataframe(data.tail(5))  # Show the latest 5 entries

    # Display Mood Trends
    plot_mood_trends(data)
else:
    st.warning("Please write something to submit.")

# Footer or additional information
st.markdown("Your privacy matters! Your journal is safe and can be deleted anytime.")
