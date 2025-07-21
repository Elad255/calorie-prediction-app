import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# UI
st.title("Calorie Prediction App")

age = st.slider("Age", 18, 80, 30)
income = st.number_input("Income", 10000, 100000, 50000)
steps = st.number_input("Steps", 0, 30000, 5000)
sleep = st.slider("Sleep Hours", 0.0, 12.0, 7.0)

if st.button("Predict"):
    input_data = scaler.transform([[age, income, steps, sleep]])
    result = model.predict(input_data)
    st.success(f"Predicted Calories: {result[0]:.2f}")
