import streamlit as st
from sentiment_analysis import analyze_sentiment
from lstm_model import predict_mood_trends

def main():
    st.title("MindEase AI Mood Tracker")

    # Sentiment analysis section
    st.header("Track Your Mood")
    text_input = st.text_area("Write what's on your mind:")
    
    if text_input:
        sentiment_score = analyze_sentiment(text_input)
        if sentiment_score > 0:
            st.write(f"You're feeling positive! Sentiment score: {sentiment_score}")
        elif sentiment_score < 0:
            st.write(f"You're feeling negative. Sentiment score: {sentiment_score}")
        else:
            st.write(f"Your sentiment is neutral. Sentiment score: {sentiment_score}")
    
    # Mood prediction section
    st.header("Mood Trend Prediction")
    mood_data_input = st.text_area("Enter your past mood scores (comma-separated):")
    
    if mood_data_input:
        mood_data = list(map(float, mood_data_input.split(',')))
        predicted_mood = predict_mood_trends(mood_data)
        st.write(f"Predicted mood trend: {predicted_mood}")

if __name__ == "__main__":
    main()




