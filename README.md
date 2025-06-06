# Heart-Disease-Prediction

- A simple and intelligent web app to predict heart disease using Machine Learning and Streamlit.

# Overview
- This is a machine learning project that predicts the likelihood of a person having heart disease based on user-input medical features.
- Built using Python, trained on real heart disease data, and deployed using Streamlit.
- Users can enter details like age, chest pain type, cholesterol level, and more to get instant predictions.
- Aimed at increasing awareness and assisting early diagnosis using a simple and user-friendly interface.

# Why Heart Disease Prediction?
- Easy & Fast Detection – Just enter the values and get results instantly.
- User-Friendly Interface – No need to understand the model, just use the web form.
- Health Education – Displays helpful resources when a person is at risk.
- No Setup Required – Runs directly in your browser using Streamlit.

# How it works
- A trained machine learning model (Logistic Regression / Random Forest) is saved as model_heart.pkl.
- The model uses key features such as:
  - Age, Sex, Chest Pain Type
  - Resting Blood Pressure, Cholesterol, Fasting Blood Sugar
  - ECG Results, Maximum Heart Rate, Exercise-Induced Angina
  - ST Depression, ST Slope, Major Vessels, and Thalassemia type
- Based on the input values, the model outputs:
  - 1 → Person likely has heart disease
  - 0 → Person is likely healthy

# How to Use
- Run the app using Streamlit:
  - streamlit run app.py
- Enter the values in the form.
- Click Detect the Heart Disease to get results.
- Red alert = risk detected. Green alert = healthy condition.

# Files in This Project
- heart.py – Main application file with Streamlit code.
- model_heart.pkl – Trained machine learning model.
- heart.csv – Dataset used for training.
- README.md – Project documentation.

# Input Features Used
- Age
- Sex (0 = Female, 1 = Male)
- Chest Pain Type (0 to 3)
- Resting Blood Pressure
- Cholesterol Level
- Fasting Blood Sugar (>120 mg/dl: 1, else 0)
- Resting ECG Results (0, 1, 2)
- Maximum Heart Rate
- Exercise-Induced Angina (1 = Yes, 0 = No)
- Oldpeak – ST depression induced by exercise
- ST Slope (0 = Upsloping, 1 = Flat, 2 = Downsloping)
- Number of Major Vessels (0–3)
- Thalassemia (1 = Fixed Defect, 2 = Normal, 3 = Reversible Defect)

# License 
- This is absolutely free and anyone can modify it and use it without any restrictions!
