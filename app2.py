import streamlit as st
import requests



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
