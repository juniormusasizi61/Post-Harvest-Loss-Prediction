from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Paths to your saved model artifacts (adjust if your folder structure changes)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
MODEL_DIR = os.path.join(BASE_DIR, 'notebooks', 'model_files')

model_path = os.path.join(MODEL_DIR, 'best_rf.pkl')
scaler_path = os.path.join(MODEL_DIR, 'scaler.pkl')
features_path = os.path.join(MODEL_DIR, 'selected_features.pkl')

# Load model, scaler, and selected features
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
selected_features = joblib.load(features_path)

@app.route('/')
def home():
    return "Post-Harvest Loss Prediction API is running! Use POST /predict to get predictions."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        # Convert input JSON to DataFrame
        df = pd.DataFrame([data])

        # Scale features
        scaled = scaler.transform(df)
        scaled_df = pd.DataFrame(scaled, columns=df.columns)

        # Select features in correct order
        input_data = scaled_df[selected_features]

        # Predict
        prediction = model.predict(input_data)[0]

        return jsonify({'predicted_loss_percent': round(float(prediction), 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
