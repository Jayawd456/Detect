'''from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(_name_)
CORS(app)  # Enables cross-origin requests from frontend

# Load the trained ML model and vectorizer
model = joblib.load("disease_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/")
def home():
    return "Disease Prediction API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        symptoms = data.get("symptoms", "")

        if not symptoms:
            return jsonify({"error": "No symptoms provided"}), 400

        # Convert input symptoms to model format
        symptoms_vector = vectorizer.transform([symptoms])

        # Get the predicted disease
        prediction = model.predict(symptoms_vector)[0]

        return jsonify({"disease": prediction})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if _name_ == "_main_":
    app.run(debug=True, port=5000)
    '''
from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(_name_)
CORS(app)  # Enables cross-origin requests from frontend

# Load the trained ML model and vectorizer
model = joblib.load("disease_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/")
def home():
    return "Disease Prediction API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get the symptoms from the form data (instead of JSON)
        symptoms = request.form.get("symptoms", "")

        if not symptoms:
            return jsonify({"error": "No symptoms provided"}), 400

        # Convert input symptoms to model format
        symptoms_vector = vectorizer.transform([symptoms])

        # Get the predicted disease
        prediction = model.predict(symptoms_vector)[0]

        return jsonify({"prediction": prediction, "details": "This is a preliminary analysis. Consult a doctor for medical advice."})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if _name_ == "_main_":
    app.run(debug=True, port=5000)