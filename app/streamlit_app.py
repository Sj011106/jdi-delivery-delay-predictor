import streamlit as st
import joblib
import numpy as np

# ── Page Config ───────────────────────────────
st.set_page_config(
    page_title="JDI Delivery Delay Predictor",
    page_icon="🚛",
    layout="centered"
)

# ── Load Model ────────────────────────────────
model = joblib.load('models/best_model.pkl')

# ── Header ────────────────────────────────────
st.title("🚛 JDI Delivery Delay Predictor")
st.markdown("Enter delivery details to predict whether it will arrive **on time or delayed.**")
st.divider()

# ── Input Form ────────────────────────────────
st.subheader("Delivery Details")

col1, col2 = st.columns(2)

with col1:
    distance = st.slider(
        "Distance (km)", 
        min_value=50, 
        max_value=800, 
        value=200,
        help="Total distance of the delivery route"
    )
    
    weather = st.selectbox(
        "Weather Severity",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: {
            1: "1 — Clear",
            2: "2 — Cloudy", 
            3: "3 — Rain",
            4: "4 — Heavy Rain",
            5: "5 — Blizzard"
        }[x]
    )
    
    road = st.radio(
        "Road Type",
        options=["Highway", "Rural"]
    )

with col2:
    season = st.selectbox(
        "Season",
        options=["Winter", "Spring", "Summer", "Fall"]
    )
    
    cargo = st.slider(
        "Cargo Weight (kg)",
        min_value=500,
        max_value=20000,
        value=5000,
        step=500
    )
    
    experience = st.slider(
        "Driver Experience (years)",
        min_value=0,
        max_value=30,
        value=5
    )
    
    hour = st.slider(
        "Departure Hour",
        min_value=4,
        max_value=22,
        value=8,
        format="%d:00"
    )

st.divider()

# ── Predict Button ────────────────────────────
if st.button("🔍 Predict Delivery Status", use_container_width=True):

    # Normalize numerical inputs
    # Must match exactly how training data was normalized
    distance_norm   = (distance - 50)   / (800 - 50)
    cargo_norm      = (cargo - 500)     / (20000 - 500)
    experience_norm = (experience - 0)  / (30 - 0)
    hour_norm       = (hour - 4)        / (22 - 4)

    # Encode road type
    road_encoded = 0 if road == "Highway" else 1

    # Encode season as one hot
    season_fall   = 1 if season == "Fall"   else 0
    season_spring = 1 if season == "Spring" else 0
    season_summer = 1 if season == "Summer" else 0
    season_winter = 1 if season == "Winter" else 0

    # Build feature array — must match training column order
    features = np.array([[
        distance_norm,
        weather,
        road_encoded,
        cargo_norm,
        experience_norm,
        hour_norm,
        season_fall,
        season_spring,
        season_summer,
        season_winter
    ]])

    # Run model
    prediction  = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    # ── Show Result ───────────────────────────
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f"⚠️ LIKELY DELAYED — {probability:.0%} confidence")
        st.markdown("**Recommendation:** Contact customer proactively and consider rescheduling.")
    else:
        st.success(f"✅ LIKELY ON TIME — {1-probability:.0%} confidence")
        st.markdown("**Recommendation:** Delivery looks good to proceed as planned.")

    # ── Show Input Summary ────────────────────
    st.divider()
    st.subheader("Delivery Summary")

    col3, col4, col5 = st.columns(3)
    col3.metric("Distance",    f"{distance} km")
    col4.metric("Weather",     f"Level {weather}/5")
    col5.metric("Road Type",   road)

    col6, col7, col8 = st.columns(3)
    col6.metric("Season",      season)
    col7.metric("Cargo",       f"{cargo:,} kg")
    col8.metric("Driver Exp",  f"{experience} yrs")