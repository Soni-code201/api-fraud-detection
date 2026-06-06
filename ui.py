import streamlit as st
import requests

st.title("💳 UPI Fraud Detection System")

st.write("Enter transaction details:")

amount = st.number_input("Amount", value=5000)
time = st.slider("Transaction Time (hour)", 0, 23, 12)
location_change = st.selectbox("Location Changed?", [0, 1])
device_change = st.selectbox("Device Changed?", [0, 1])
transaction_count = st.number_input("Transaction Count", value=1)
failed_attempts = st.number_input("Failed Attempts", value=0)
account_age = st.number_input("Account Age (days)", value=100)

if st.button("Check Fraud"):
    url = "http://127.0.0.1:8000/predict"

    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()
        st.subheader("Result:")
        st.write(result)
    else:
        st.error("API not running!")