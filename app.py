import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("california_house_model.pkl")

st.title("🏠 California House Price Predictor")

st.write(
    "Enter housing details below and click Predict."
)

medinc = st.number_input("Median Income", value=5.0)
houseage = st.number_input("House Age", value=20.0)
averooms = st.number_input("Average Rooms", value=6.0)
avebedrms = st.number_input("Average Bedrooms", value=1.0)
population = st.number_input("Population", value=1000.0)
aveoccup = st.number_input("Average Occupancy", value=3.0)
latitude = st.number_input("Latitude", value=34.0)
longitude = st.number_input("Longitude", value=-118.0)

if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "MedInc": [medinc],
        "HouseAge": [houseage],
        "AveRooms": [averooms],
        "AveBedrms": [avebedrms],
        "Population": [population],
        "AveOccup": [aveoccup],
        "Latitude": [latitude],
        "Longitude": [longitude]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted House Value: {prediction[0]:.3f}"
    )