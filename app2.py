import streamlit as st
import requests
import os

url_lstm = 'https://sebnb-930802109890.europe-west1.run.app/lstm'
string = st.text_input('input a string')
params = {'st' : string}

response = requests.get(url_lstm, params).json()
pred = response.get('answer')
st.write(f'YAAAAAYY the prediction is {pred}')
