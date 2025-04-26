# Post-Harvest Loss Prediction API & Web App

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Installation](#installation)  
- [Usage](#usage)  
  - [Run Flask API](#run-flask-api)  
  - [Run Streamlit UI](#run-streamlit-ui)  
- [API Endpoint](#api-endpoint)  
- [Project Structure](#project-structure)  
- [Model Details](#model-details)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

---

## Project Overview

This project is a **Post-Harvest Loss Prediction** tool designed to estimate the percentage loss of crops based on environmental and storage factors. It provides:

- A **Flask REST API** that serves a trained machine learning model for prediction.
- A **Streamlit web interface** for easy, interactive user input and instant prediction results.

This solution helps farmers and stakeholders reduce losses by enabling informed decisions.

---

## Features

- Predict crop loss percentage based on temperature, humidity, rainfall, storage days, and crop type.
- RESTful API endpoint for integration with other applications.
- Interactive web UI with Streamlit — no frontend coding required.
- Scalable and easy to deploy.

---

## Tech Stack

- **Backend:** Python, Flask, scikit-learn, joblib  
- **Frontend:** Streamlit  
- **Model:** Random Forest Regressor (pre-trained)  
- **Environment:** Python 3.12+  

---

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/post-harvest-loss-prediction.git
cd post-harvest-loss-prediction


2. (Optional but recommended) Create and activate a virtual environment:

python -m venv venv

Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate


3. Install dependencies:

pip install -r requirements.txt


---

## Usage

### Run Flask API

Start the Flask server to serve the prediction API:

python app.py


The API will be available at `http://127.0.0.1:5000/`.

### Run Streamlit UI

In a new terminal window, run the Streamlit app:

streamlit run streamlit_app.py


This opens a web UI in your default browser for interactive predictions.

---

## API Endpoint

- **POST** `/predict`

  - **Description:** Predict the post-harvest loss percentage.
  - **Request Body (JSON):**

    ```
    {
      "temperature": 28,
      "humidity": 70,
      "rainfall": 50,
      "storage_days": 10,
      "crop_type": 1
    }
    ```

  - **Response:**

    ```
    {
      "predicted_loss_percent": 12.34
    }
    ```

---

## Project Structure




---

## Model Details

- Model: Random Forest Regressor trained on historical crop and environmental data.
- Features used: temperature, humidity, rainfall, storage_days, crop_type.
- Data preprocessing includes feature scaling and feature selection.

---

## Contributing

Contributions are welcome! Please open issues or pull requests for bug fixes, improvements, or new features.


---

browse the app 
(https://agripredictmodel.streamlit.app/)

## Contact

- **Your Name**  
- Email: juniormusasizi6@gmail.com
- GitHub: [juniormusasizi61](https://github.com/juniormusasizi61) 
- LinkedIn: [Musasizi Junior](https://www.linkedin.com/in/musasizi-junior-291012247/)

# 🎉 Thank you for checking out this project! 🎉
