from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib
import re


def preprocess_data(code):
    # vba code cleaning and preprocessing

    # Normalize hexadecimal strings (example: replace hex strings with a placeholder or decode)
    cleaned_code = re.sub(r'(?:0x)?[0-9A-Fa-f]{2,}', ' hexstring ', code)

    # Normalize whitespace and lowercase
    cleaned_code = re.sub(r"\s+", ' ', cleaned_code).strip().lower()

    return cleaned_code


def calculate_extra_features(code):
    pattern = r"[ \t\n\r\f\v]+|[;(){}.,:+-/*=&<>]|\"[^\"]*\"|'[^']*'"
    tokens = re.split(pattern, code)

    tokens = [token for token in tokens if token]
    lengths = [len(token) for token in tokens]

    if len(lengths) > 0:
        max_length = max(lengths)
    else:
        max_length = 0

    return len(code), len(code.splitlines()), len(tokens), max_length


def get_extra_features(data):
    extra_features = [calculate_extra_features(code) for code in data if code]
    return extra_features


def extract_features(data, vectorizer=None, mode='train'):

    extra_features_vectors = get_extra_features(data)

    # If in training mode, fit the vectorizer on the data first
    if mode == 'train':
        vectorizer = TfidfVectorizer(max_features=1000)
        tfidf_vectors = vectorizer.fit_transform(data)
    else:
        tfidf_vectors = vectorizer.transform(data)

    vectors = np.concatenate((tfidf_vectors.toarray(), extra_features_vectors), axis=1)
    return vectors, vectorizer


def load_model(path):
    return joblib.load(path)


def save_model(model, path):
    joblib.dump(model, path)


def load_vectorizer(path):
    return joblib.load(path)


def save_vectorizer(vectorizer, path):
    joblib.dump(vectorizer, path)
