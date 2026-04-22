# (yaha poora Streamlit code paste kar)
import streamlit as st
import numpy as np
import pickle

# load your trained model
model = pickle.load(open('ridgemodel.pkl', 'rb'))

st.title("🏠 House Price Prediction")

# Inputs
area = st.number_input("Area (sq ft)", min_value=0)
bed = st.number_input("Bedrooms", min_value=0)
bath = st.number_input("Bathrooms", min_value=0)
location = st.selectbox("Location", ["Banjara Layout", "Whitefield", "Indiranagar"])

# Predict button
if st.button("Predict"):
    try:
        # example input (modify according to your model)
        input_data = np.array([[area, bed, bath, 0]])  # location encoding change karna padega

        price = model.predict(input_data)[0]

        if price < 0:
            st.error("⚠ Invalid input / unrealistic house details")
        else:
            st.success(f"💰 Price: {round(price, 2)} Lacs")

    except Exception as e:
        st.error(f"Error: {e}")
