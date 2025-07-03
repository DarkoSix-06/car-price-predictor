![Screenshot_3-7-2025_04117_localhost](https://github.com/user-attachments/assets/76a30b50-2b95-4ad6-ac87-fdba8763386e)

# 🚗 Car Price Predictor

This project is a **machine learning web application** that predicts the selling price of a used car based on input features. It's built with **Python (Flask)** for the backend, **React.js** for the frontend, and **Tailwind CSS** for UI styling. The machine learning model is a trained **Random Forest Regressor**.

---

## ✨ Features

- 🔮 Predict resale value of a car based on key features
- ⚙️ Flask backend with REST API for predictions
- 🖥️ React + TailwindCSS frontend
- 💡 Clean UI with input validation and live prediction

---

## 📊 Input Features

| Feature             | Description                              |
|---------------------|------------------------------------------|
| Present Price (₹)   | Original price of the car (new)          |
| Kilometers Driven   | How many kilometers the car has been used |
| Car Age             | Age of the car in years                  |
| Fuel Type           | Petrol / Diesel                          |
| Seller Type         | Dealer / Individual                      |
| Transmission        | Manual / Automatic                       |
| Owner Type          | 0 = First, 1 = Second, ..., 4 = Test Drive |

---

## 🧪 Model Metrics

| Metric   | Value     |
|----------|-----------|
| MAE      | ~76,000 ₹ |
| RMSE     | ~1.57 Lakhs |
| R² Score | ~0.96     |

Model: RandomForestRegressor  
Trained on: Cleaned version of `Car details v3.csv`

---

## 🛠 Tech Stack

| Layer    | Technology           |
|----------|----------------------|
| Frontend | React.js, Tailwind CSS |
| Backend  | Flask (Python)       |
| ML Model | Scikit-learn (Random Forest) |

---

📁 Project Structure

car-price-predictor/
│
├── backend/
│   ├── app.py
│   ├── car_price_model.pkl
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   └── App.js
│   ├── tailwind.config.js
│   └── ...
│
├── Car details v3.csv
└── README.md

---
📌 License
This project is for educational/demo purposes. Feel free to fork and build upon it!

----
🧠 Example Prediction
Input:

Present Price: ₹500000

KM Driven: 35000

Car Age: 5

Fuel: Petrol

Seller Type: Individual

Transmission: Manual

Owner: First

🔮 Output:

Estimated Selling Price: ₹4.08 Lakhs
