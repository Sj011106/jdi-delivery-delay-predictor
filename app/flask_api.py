from flask import Flask, request, jsonify
import joblib
import numpy as np

# ── Create the Flask app ──────────────────────
app = Flask(__name__)

# ── Load model once when server starts ────────
# This runs ONCE at startup, not on every request
model = joblib.load('models/best_model.pkl')

print("Model loaded successfully!")
print(f"Model type: {type(model).__name__}")
# ── Health check endpoint ──────────────────────
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'running'})
# ── Prediction endpoint ────────────────────────
@app.route('/predict', methods=['POST'])
def predict():
    # Step 1 — Read incoming JSON data
    data = request.json
    print(f"Received data: {data}")
    # Step 2 — Extract each feature from the request
    distance          = data['distance_km']
    weather           = data['weather_severity']
    cargo             = data['cargo_weight_kg']
    experience        = data['driver_experience_yrs']
    hour              = data['departure_hour']
    road_type         = data['road_type']
    season_fall       = data['season_fall']
    season_spring     = data['season_spring']
    season_summer     = data['season_summer']
    season_winter     = data['season_winter']

    # Step 3 — Arrange features in exact same order as training data
    features = np.array([[
        distance,
        weather,
        road_type,
        cargo,
        experience,
        hour,
        season_fall,
        season_spring,
        season_summer,
        season_winter
    ]])

    # Step 4 — Run the model
    prediction  = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    # Step 5 — Build and return response
    result = {
        'delayed':     bool(prediction),
        'probability': round(float(probability), 3),
        'message':     'DELAYED' if prediction == 1 else 'ON TIME'
    }

    print(f"Prediction: {result}")
    return jsonify(result)
# ── Run the server ─────────────────────────────
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )