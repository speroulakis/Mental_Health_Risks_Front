import streamlit as st
import requests
import matplotlib.pyplot as plt
from scipy import misc

st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("PharmaFeel")


url_lstm = 'https://sebnb-930802109890.europe-west1.run.app/lstm'

st.write('This project uses NLP (Natural Naguage Processing) to predict the sentiment carried by a sentence when reviewing drugs')

string = st.text_area('Review : ')

if string :

    params = {'st' : string}

    response = requests.get(url_lstm, params).json()
    pred = response.get('answer')
    if pred >= 0.5:
        ans = 'Good/Positive'
    else :
        ans = 'Bad/Negative'
    st.write(f'Feeling detected : {ans}, with a score of {round(pred,2)}')


else :
    st.warning('Please enter some input')



# Texte unique
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
