import os
import streamlit as st
import requests


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
url = BASE_URI + '/predict'

st.title("Mental Health Risks predictor")

st.markdown('''This project focuses on developing a natural language processing (NLP)
          model to predict the likelihood of a patient exhibiting risky behaviors associated with mental health conditions.
          By analyzing text data, the model identifies patterns that may indicate tendencies toward risky behaviors,
          assisting mental health professionals in early detection and intervention''')

user_input = st.text_input("Enter some data:")

params = {
    'st' : user_input
}
response = requests.get(url, params=params)

if response.status_code == 200:
    prediction = response.json()
    st.write(f"Prediction: {prediction.get('prediction')}")
else:
    st.write("Failed to get a valid response from the API.")









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
