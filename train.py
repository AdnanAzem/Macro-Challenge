import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from model_utils import preprocess_data, extract_features, save_model, save_vectorizer
from sklearn.ensemble import RandomForestClassifier

# Load training and test data
train_data_path = 'data/train_dataset.csv'
test_data_path = 'data/validation_dataset.csv'

print("loading data")
train_df = pd.read_csv(train_data_path, encoding='ascii', encoding_errors='ignore')
test_df = pd.read_csv(test_data_path, encoding='ascii', encoding_errors='ignore')

print("preprocessing data")
# Assuming the last column is the target variable
X_train_raw = train_df.loc[:, 'vba_code'].values
y_train = train_df.loc[:, 'label']

X_test_raw = test_df.loc[:, 'vba_code'].values
y_test = test_df.loc[:, 'label']

# Preprocess the data
X_train_preprocessed = [preprocess_data(code) for code in X_train_raw]
X_test_preprocessed = [preprocess_data(code) for code in X_test_raw]

print("extract features")
# Feature extraction - TF-IDF
X_train_features, vectorizer = extract_features(X_train_preprocessed, mode='train')
X_test_features, _ = extract_features(X_test_preprocessed, vectorizer=vectorizer, mode='predict')

print("ML model training")
# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_features, y_train)

print("Save trained model and vectorizer")
# Save the model and vectorizer for later use
save_model(model, 'model/vba_code_mal_detection_rf_model.joblib')
save_vectorizer(vectorizer, 'model/vba_code_tfidf_vectorizer.joblib')

# Predictions and performance evaluation on the test set
predictions = model.predict(X_test_features)
accuracy = accuracy_score(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.5f}%")
print(f"Confusion Matrix:\n{conf_matrix}")