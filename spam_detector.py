import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import config

def train_detector():
    data = pd.read_csv("spam_dataset.csv")  # Dataset should contain 'text' and 'label' columns
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data["text"])
    y = data["label"]

    model = MultinomialNB()
    model.fit(X, y)

    with open("spam_model.pkl", "wb") as f:
        pickle.dump((vectorizer, model), f)

def load_spam_model():
    with open(config.SPAM_MODEL, "rb") as f:
        return pickle.load(f)

def is_spam_email(email_body):
    vectorizer, model = load_spam_model()
    email_vector = vectorizer.transform([email_body])
    return model.predict(email_vector)[0] == "spam"
