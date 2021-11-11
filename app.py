# pip install streamlit
import streamlit as st
from model import predict_duration
import numpy as np

st.set_page_config(page_title="Seoul Bike Trip Duration Prediction App",
                   page_icon="🛴", layout="wide")


with st.form("prediction_form"):

    st.header("Enter the Details:")

    distance = st.number_input("Distance: ", value=0, format="%d")
    haversine = st.number_input("Haversine: ", value =0, format = "%d")
    phour = st.slider("Pickup Hour: ", 0, 23, value=0, format="%d")
    pmin = st.slider("Pickup Minute: ", 0, 59, value=0, format="%d")
    dhour = st.slider("Dropoff Hour: ", 0, 23, value=0, format="%d")
    dmin = st.slider("Dropoff Minute: ", 0, 59, value=0, format="%d")
    temp = st.number_input("Temperature: ", value = 0, format = "%d")
    humid = st.number_input("Humidity: ", value = 0, format = "%d")
    solar = st.number_input("Solar: ", value = 0, format = "%d")
    groundtemp = st.number_input("Ground Temperature: ", value = 0, format = "%d")
    dust = st.number_input("Dust: ", value = 0, format = "%d")

    submit_val = st.form_submit_button("Predict Duration")

if submit_val:
    # If submit is pressed == True
    attribute = np.array([distance, haversine,
                        pmin, dhour,
                        dmin, temp,
                        humid, solar, groundtemp, dust]).reshape(1,-1)


    if attribute.shape == (1,10):
        print("attributes valid")
        

        value = predict_duration(attributes= attribute)


        st.header("Here are the results:")
        st.success(f"The Duration predicted is {value} mins")