![Brief-5](Brief-5.jpg "Brief-5")
# BRIEF 3
## Développer une API REST pour exposer un modèle prédictif avec des données immobilières

### Récupération d'un modèle ML et développement d'une API pour l'exposer.

## Contexte du projet: 
En tant que DEV IA vous avez été chargé d'intégrer un modèle prédictif fourni par un data scientist dans une application destinée à une agence immobilière. 
Pour cela vous allez commencer par développer une API avec FastAPI qui expose le modèle en question.



# Real Estate Price Prediction API

## Description
This program implements a FastAPI API for predicting real estate prices per square meter. It utilizes two pre-trained models to make predictions based on various features such as geolocation, number of rooms, living area, postal code, etc. The models are saved in pickle format ('optimal_rfr_model.pkl' and 'optimal_linear_regression_model.pkl').

## Steps
1. Load real estate data from a CSV file ('transactions_upload.csv').
2. Clean and enrich the data, calculating the price per square meter.
3. Filter real estate transactions in Île-de-France for the year 2022.
4. Select relevant features and calculate surface sums.
5. Convert categories into binary variables (dummies).
6. Convert the date into the number of days since January 1, 1970.
7. Save the processed data to a CSV file ('transactions_idf.csv').
8. Set up a FastAPI API with two routes to predict the price per square meter based on geolocation and other features.

## Used Models
- 'optimal_rfr_model.pkl': Random Forest Regression Model.
- 'optimal_linear_regression_model.pkl': Linear Regression Model.

## API Endpoints
1. `/prix_m2`: Predicts the price per square meter based on longitude and latitude.
2. `/prix_m2_two`: Predicts the price per square meter based on the number of rooms, living area, price per square meter, postal code, longitude, and latitude.

## Installation and Usage
1. Clone the repository.
2. Install the required dependencies (`pip install -r requirements.txt`).
3. Run the FastAPI application using uvicorn (`uvicorn app:app --reload`).

## Models
The pre-trained models are stored in the following files:
- 'optimal_rfr_model.pkl'
- 'optimal_linear_regression_model.pkl'

## Example Usage
### Predict Price per Square Meter by Geolocation
```python
import requests

url = "http://127.0.0.1:8000/prix_m2"
payload = {"longitude": 2.3522, "latitude": 48.8566}
response = requests.post(url, data=payload)
print(response.json())

# Predict Price per Square Meter by Multiple Features

'''
import requests

url = "http://127.0.0.1:8000/prix_m2_two"
payload = {
    "n_pieces": 3,
    "surface_habitable": 120.0,
    "prix_m2": 9000.0,
    "code_postal": 75001,
    "longitude": 2.3522,
    "latitude": 48.8566,
}
response = requests.post(url, data=payload)
print(response.json())

'''

Predict Price per Square Meter by Multiple Features

'''
import requests

url = "http://127.0.0.1:8000/prix_m2_two"
payload = {
    "n_pieces": 3,
    "surface_habitable": 120.0,
    "prix_m2": 9000.0,
    "code_postal": 75001,
    "longitude": 2.3522,
    "latitude": 48.8566,
}
response = requests.post(url, data=payload)
print(response.json())
'''

Note: Adjust the API URL and payload accordingly.
# Requirements

    FastAPI
    uvicorn
    pickle
    scikit-learn
    pandas
    matplotlib
    numpy

# Author
Olivier LAVAUD
