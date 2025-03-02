import streamlit as st
from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

st.title("Sentiment Analyzer for Movie Reviews")

review = st.text_area("Enter your movie review:", "")

if st.button('Predict Sentiment'):
    if review:
        prediction = sentiment_analyzer(review)[0]
        st.write(f"Prediction: {prediction['label']}")
        st.write(f"Confidence: {prediction['score']:.4f}")
    else:
        st.write("Please enter a review to analyze.")
