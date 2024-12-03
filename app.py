import os
import streamlit as st
import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import random


# Define the base URI of the API
#   - Potential sources are in `.streamlit/secrets.toml` or in the Secrets section
#     on Streamlit Cloud
#   - The source selected is based on the shell variable passend when launching streamlit
#     (shortcuts are included in Makefile). By default it takes the cloud API url
if 'API_URI' in os.environ:
    BASE_URI = st.secrets[os.environ.get('API_URI')]
else:
    BASE_URI = st.secrets['cloud_api_uri']
BASE_URI = BASE_URI if BASE_URI.endswith('/') else BASE_URI + '/'
# Add a '/' at the end if it's not there
# Define the url to be used by requests.get to get a prediction (adapt if needed)

# URL de l'API FastAPI
url = BASE_URI + '/predict'

# Fonction pour appeler l'API FastAPI
def call_api(text):
    payload = {"text": text}
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result.get("prediction", "Unknown"), result.get("confidence", 0)
        else:
            st.error(f"Erreur API : {response.status_code}")
            return "Erreur", 0
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur de connexion à l'API : {e}")
        return "Erreur", 0

# Interface Streamlit
st.title("PharmaFeel")

# Choix du mode d'entrée
st.sidebar.header("Options")
input_method = st.sidebar.selectbox("Data Type", ["Feeling", "CSV File"])

# Texte unique
if input_method == "Feeling":
    text_input = st.text_area("How do you feel :", "")
    if st.button("Analyze"):
        if text_input.strip():
            params2 = {
                'st' : text_input}
            response = requests.get(url, params=params2)
            jean = response.json().get("prediction")
            #sentiment, confidence = call_api(text_input)
            st.write(f"**Feeling detected:** {jean}")
            #st.write(f"**Confiance :** {response:.2f}")
        else:
            st.warning("Please enter text.")

# Fichier CSV
else:
    uploaded_file = st.file_uploader("Importer un fichier CSV contenant des retours patients :", type="csv")
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write("Aperçu des données :")
        st.write(data.head())

        if st.button("Analyser le fichier"):
            if not data.empty:
                # Analyse chaque ligne du fichier
                data["Sentiment"] = data.iloc[:, 0].apply(lambda x: call_api(x)[0])
                data["Confidence"] = data.iloc[:, 0].apply(lambda x: call_api(x)[1])

                # Afficher les résultats
                st.write("Données analysées :")
                st.write(data[["Sentiment", "Confidence"]])

                # Graphique des résultats
                st.subheader("Répartition des sentiments")
                sentiment_counts = data["Sentiment"].value_counts()
                fig, ax = plt.subplots()
                ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
                ax.axis('equal')
                st.pyplot(fig)

                # Nuage de mots pour les sentiments positifs
                positive_texts = " ".join(data[data["Sentiment"] == "positive"].iloc[:, 0].values)
                if positive_texts.strip():
                    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(positive_texts)
                    st.subheader("Nuage de mots - Sentiments positifs")
                    st.image(wordcloud.to_array())
                else:
                    st.write("Pas de texte positif pour générer un nuage de mots.")
            else:
                st.warning("Le fichier est vide.")






# TODO: Call the API using the user's input
#   - url is already defined above
#   - create a params dict based on the user's input
#   - finally call your API using the requests package


# TODO: retrieve the results
#   - add a little check if you got an ok response (status code 200) or something else
#   - retrieve the prediction from the JSON


# TODO: display the prediction in some fancy way to the user


# TODO: [OPTIONAL] maybe you can add some other pages?
#   - some statistical data you collected in graphs
#   - description of your product
#   - a 'Who are we?'-page
