from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

# Create Flask app and enable CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load trained ML model
model = joblib.load('car_price_model.pkl')

# Optional: test route
@app.route('/')
def index():
    return "✅ Flask backend is running."

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)  # 👈 debug log

        features = [
            data['present_price'],
            data['kms_driven'],
            data['car_age'],
            data['fuel_type_diesel'],
            data['fuel_type_petrol'],
            data['seller_type_individual'],
            data['transmission_manual'],
            data['owner']
        ]

        prediction = model.predict([features])[0]
        return jsonify({'predicted_price': round(prediction, 2)})

    except Exception as e:
        print("Prediction error:", e)
        return jsonify({'error': str(e)}), 500


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
