import pandas as pd
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from scipy.special import softmax
import streamlit as st
import numpy as np
import io

# Streamlit app code
st.title("Sentiment Analysis App")

st.header("Enter the Sentiment here:")
    # Input text from the user
user_input = st.text_area(" ", height=100)

    # Preprocess Text
user_input_word = []

if st.button("Predict"):
        for word in user_input.split(' '):
            if word.startswith('@') and len(word) > 1:
                word = '@user'
            elif word.startswith('http'):
                word = "http"
            user_input_word.append(word)

        user_input_processed = " ".join(user_input_word)

        # Load the model
        roberta = "cardiffnlp/twitter-roberta-base-sentiment"

        model = AutoModelForSequenceClassification.from_pretrained(roberta)

        tokenizer = AutoTokenizer.from_pretrained(roberta)

        labels = ['Negative', 'Neutral', 'Positive']

        encoded_text = tokenizer(user_input_processed, return_tensors='pt')
        output = model(**encoded_text)
        scores = output.logits.detach().numpy()
        scores = softmax(scores, axis=1)

        ranking = np.argsort(scores.squeeze())[::-1]

        st.subheader("Prediction Results:")
        for i in range(scores.shape[1]):
            l = labels[ranking[i]]
            s = scores.squeeze()[ranking[i]]
            st.write(f"{i + 1}) {l}: {np.round(float(s), 4)}")