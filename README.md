#🏡 House Price Predictor


#💼 Industry Project
This project was developed as part of an industry-level assignment, applying machine learning techniques and full-stack development to solve a real-world problem in housing price estimation.

A web-based application that predicts house prices using user input (bedrooms, bathrooms, size, ZIP code), powered by a trained machine learning model and a Flask backend.



## ✅ Project Overview

This project demonstrates:
- Frontend development using **HTML, CSS, JavaScript**
- Backend integration using **Flask (Python)**
- Model training using **scikit-learn**
- Model serialization using **joblib**


🔹 1. Project Planning and Objective
I started by clearly defining the goal:

To build a simple and interactive web application that predicts house prices based on user input like number of bedrooms, bathrooms, square footage, and ZIP code.

🔹 2. Data Collection and Model Training
I used a publicly available real estate dataset (or simulated structured housing data) that includes features like bedrooms, bathrooms, square footage, and ZIP code.

Cleaned and preprocessed the data (handled missing values, converted data types, etc.)

Selected Linear Regression as the prediction algorithm due to its simplicity and suitability for price prediction problems.

Trained the model using scikit-learn and tested accuracy.

Exported the trained model using joblib to allow reuse in the backend without retraining.

🔹 3. Setting Up the Project Structure
I organized the project into three main parts:

index.html: Frontend form for user input.

script.js: JavaScript for dynamic frontend behavior.

app.py: Flask backend handling input, prediction, and routing.

model.pkl: Serialized trained ML model used by Flask.

🔹 4. Frontend Development
I built a responsive HTML form where users can enter:

Number of bedrooms

Number of bathrooms

Size (in sq ft)

ZIP code

I styled it using CSS and added JavaScript to:

Collect form data

Send a request to the backend

Display the prediction result

🔹 5. Flask Backend Integration
Created a Flask application (app.py) with:

A route to serve the HTML page

A POST API route (/predict) to handle prediction logic

The backend:

Receives form data via JSON

Loads the trained model using joblib

Passes user input to the model

🔹 6. Connecting Frontend and Backend
Using JavaScript's fetch() API:

The form data is sent to the Flask /predict endpoint.

The response from the backend is displayed dynamically on the page without reloading.

Users get an instant and interactive prediction experience.

🛠️ Technologies Used
Python

Flask

scikit-learn

HTML, CSS, JavaScript

joblib for model serialization

