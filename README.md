# 🥗 Calorie Prediction App

A simple machine learning-powered web app that predicts daily calorie expenditure based on user input: age, income, daily steps, and sleep hours.

## Live Demo

This app was built with **Streamlit** and can be deployed using **localtunnel**, **ngrok**, or **Streamlit Community Cloud**.

---

##  Features

- Predicts daily calorie burn based on:
  - Age
  - Monthly income
  - Steps per day
  - Sleep duration
- Built with a trained **Linear Regression** model
- User-friendly interface using Streamlit

---

##  Technologies Used

- Python
- Scikit-learn
- Streamlit
- Joblib
- NumPy / Pandas

---

## Files Included

| File           | Description |
|----------------|-------------|
| `notebook.ipynb` | Full ML workflow: scaling, training, evaluation |
| `app.py`        | Web app interface using Streamlit |
| `model.pkl`     | Trained calorie prediction model |
| `scaler.pkl`    | Preprocessing scaler used before prediction |

---

## 📷 Screenshot

![App Screenshot](C:\Users\vardi\Downloads\screenshot.png) <!-- Optional: upload a screenshot -->

---

##  Model Performance

-  Root Mean Squared Error (RMSE)
-  R² Score

---

##  How to Run

```bash
# In your terminal
streamlit run app.py
