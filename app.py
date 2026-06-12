import streamlit as st
import pickle
import re
import string
import nltk


from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources (only first run)
nltk.download('stopwords')
nltk.download('wordnet')

# Load model and vectorizer
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# Preprocessing setup
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = str(text).lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # Remove mentions and hashtags
    text = re.sub(r'@\w+|#\w+', '', text)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra spaces
    text = text.strip()
    
    # Tokenize, remove stopwords, lemmatize
    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    
    return ' '.join(words)

# Page config
st.set_page_config(page_title="Sentiment Analyzer", page_icon="💬")

# UI
st.title("💬 Sentiment Analysis App")
st.write("Analyze sentiment of tweets or text using Machine Learning")

# Input
user_input = st.text_area("Enter your text here:")

# Prediction
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        cleaned_text = clean_text(user_input)
        vectorized_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(vectorized_text)[0]

        st.subheader("Prediction Result:")

        if prediction == "Positive":
            st.success("😊 Positive Sentiment")
        elif prediction == "Negative":
            st.error("😡 Negative Sentiment")
        else:
            st.info("😐 Neutral Sentiment")