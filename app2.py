import streamlit as st
import requests
import os

st.title("PharmaFeel")


url_lstm = 'https://sebnb-930802109890.europe-west1.run.app/lstm'
string = st.text_input('input a string')
params = {'st' : string}

response = requests.get(url_lstm, params).json()
pred = response.get('answer')
st.write(f'YAAAAAYY the prediction is {pred}')

# # Texte unique
# if input_method == "Feeling":
#     text_input = st.text_area("How do you feel :", "")
#     if st.button("Analyze"):
#         if text_input.strip():
#             params2 = {
#                 'st' : text_input}
#             response = requests.get(url, params=params2)
#             jean = response.json().get("prediction")
#             #sentiment, confidence = call_api(text_input)
#             st.write(f"**Feeling detected:** {jean}")
#             #st.write(f"**Confiance :** {response:.2f}")
#         else:
#             st.warning("Please enter text.")
