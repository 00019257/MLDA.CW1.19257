import streamlit as st
import pickle
import numpy as np

st.title("Apartment Price Prediction")
st.write("Apartment price prediction based on user chosen preferences.")

# Load Model
@st.cache_data
def load_model():
	return pickle.load(open('model.pkl', 'rb'))

model = load_model()

if model:
	st.toast('Model loaded successfully')
else:
	st.toast('Model load error. fix it mf.')

# User Inputs
square_feet = st.number_input("Square Feet", min_value=100, max_value=40000, value=950)
col1, col2, col3 = st.columns(3)
with col1:
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=9, value=1)
with col2:
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=9, value=2)
with col3:
    total_rooms = st.number_input("Total Rooms", min_value=1, max_value=15, value=3)
colA, colB = st.columns(2)
with colA:
    pets_friendly_checkbox = st.checkbox("Pet Friendly", key="pets", help="Check if pets are allowed")
with colB:
    has_photo_checkbox = st.checkbox("Has Photos", key="photos", help="Check if listing has photos")
# Convert Checkboxes
pets_friendly = int(pets_friendly_checkbox)
has_photo_binary = int(has_photo_checkbox)
latitude = st.slider("Latitude", min_value=20.0, max_value=65.0, value=40.0)
longitude = st.slider("Longitude", min_value=-160.0, max_value=-70.0, value=-95.00)
map = {
	'lat': [latitude],
	'lon': [longitude]
}
st.map(map, zoom=7)


# Prepare to Load Features Based Off User Input
features = [[
    square_feet,
    bathrooms,
    bedrooms,
    latitude,
    longitude,
    total_rooms,
    pets_friendly,
    has_photo_binary
]]

# Predict and Voila
if st.button("Predict"):
    # 'Twas For Testing
    # st.write("DEBUG – Model received these inputs:", features)
    prediction = model.predict(features)
    st.success(f"Predicted Price: ${prediction[0]:,.2f}")