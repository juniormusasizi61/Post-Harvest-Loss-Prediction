import streamlit as st
import joblib
import pandas as pd
import os

# Define paths relative to this file
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'notebooks', 'model_files')

# Load model artifacts
model = joblib.load(os.path.join(MODEL_DIR, 'best_rf.pkl'))
scaler = joblib.load(os.path.join(MODEL_DIR, 'scaler.pkl'))
selected_features = joblib.load(os.path.join(MODEL_DIR, 'selected_features.pkl'))

# Streamlit UI
st.title("Post-Harvest Loss Prediction")

temperature = st.number_input("Temperature (°C)", value=25)
humidity = st.number_input("Humidity (%)", value=60)
rainfall = st.number_input("Rainfall (mm)", value=30)
storage_days = st.number_input("Storage Days", value=10)
crop_type = st.number_input("Crop Type (numeric code)", value=1)

if st.button("Predict Loss"):
    input_dict = {
        "temperature": temperature,
        "humidity": humidity,
        "rainfall": rainfall,
        "storage_days": storage_days,
        "crop_type": crop_type
    }
    df = pd.DataFrame([input_dict])
    scaled = scaler.transform(df)
    scaled_df = pd.DataFrame(scaled, columns=df.columns)
    input_data = scaled_df[selected_features]
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Loss Percentage: {round(float(prediction), 2)}%")
