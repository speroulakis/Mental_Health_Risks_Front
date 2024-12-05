import streamlit as st
import requests
import matplotlib.pyplot as plt


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
    st.write(f'Feeling detected : {ans}, with a score of {round(pred,2)*100}')
    labels = ['Positive (1)', 'Negative (0)']
    sizes = [pred, 1 - pred]
    colors = ['#4CAF50', '#FF5733']
    explode = (0.1, 0)
    fig, ax = plt.subplots()
    ax.pie(
        sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90)
    ax.axis('equal')
    st.write("### Sentiment Analysis Prediction")
    st.pyplot(fig)


else :
    st.warning('Please enter some input')
