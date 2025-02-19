import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

def train_detector():
    data = pd.read_csv("spam_dataset.csv")  # Dataset should contain 'text' and 'label' columns
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data["text"])
    y = data["label"]

    model = MultinomialNB()
    model.fit(X, y)

    with open("spam_model.pkl", "wb") as f:
        pickle.dump((vectorizer, model), f)
