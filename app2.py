import streamlit as st
import requests
import matplotlib.pyplot as plt
import time
url_lstm = 'https://sebnb-930802109890.europe-west1.run.app/lstm'

st.set_page_config(
    page_title="PharmaFeel",
    page_icon="&#x1F48A",  # Utilisation d'un emoji comme icône
    layout="wide",
)
st.markdown("<h1 style='text-align: center;'>Welcome To PharmaFeel App 💊</h1>", unsafe_allow_html=True)
st.write("Let's analyze the sentiment of drug reviews with cutting-edge NLP techniques!")

with st.expander("ℹ️ About This App"):
    st.write(
        """
        Enter a detailed review about any medication experience.
        Be as descriptive as possible, mentioning both the positive and negative effects.
        Let AI work its magic!
        """
    )

user_input = st.text_area("Enter your drug review here:", height=150, placeholder="e.g., This drug significantly reduced my pain but caused mild nausea.")

if st.button('Analyze'):
    if user_input :

        with st.spinner('AI at work... Magic happening!'):
            # Simuler un délai pour la requête API (par exemple, 2 secondes)
            time.sleep(2)

        params = {'st' : user_input}
        response = requests.get(url_lstm, params).json()
        pred = response.get('answer')

        positive_probability = round(pred*100)
        negative_probability = 100 - positive_probability

        # Texte descriptif
        st.write(f"Positive: {positive_probability}% | Negative: {negative_probability}%")

        # Barre horizontale avec HTML/CSS
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; width: 100%; border: 1px solid #ddd; border-radius: 5px; overflow: hidden;">
                <div style="width: {positive_probability}%; background-color: #4CAF50; height: 30px; text-align: center; color: white; font-weight: bold;">
                    {positive_probability}%
                </div>
                <div style="width: {negative_probability}%; background-color: #FF5252; height: 30px; text-align: center; color: white; font-weight: bold;">
                    {negative_probability}%
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
