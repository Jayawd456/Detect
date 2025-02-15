import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Load dataset (CSV file containing Symptoms & Disease labels)
data = pd.read_csv(r"C:\Users\anura\OneDrive\Desktop\python\disease_prediction\backend\Training.csv")
# Ensure this file exists in your VS Code project

# Convert text symptoms into a format suitable for ML
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["Symptoms"])  # Convert symptoms into numerical features
y = data["Disease"]  # Target labels

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Naive Bayes Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save the trained model and vectorizer
joblib.dump(model, "disease_model.pkl")     # Saves ML model
joblib.dump(vectorizer, "vectorizer.pkl")   # Saves vectorizer

print("✅ Model trained and saved successfully!")