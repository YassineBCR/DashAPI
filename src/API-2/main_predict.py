'''
SIMPLON BRIEF-5 PHASE PREFINING

plaintext

SIMPLON BRIEF-5 PHASE FINAL

Programme: Real Estate Price Prediction API

Description:
Ce programme implémente une API FastAPI pour la prédiction du prix au mètre carré dans le secteur immobilier. Deux modèles pré-entrainés sont utilisés pour effectuer des prédictions en fonction de différentes caractéristiques telles que la géolocalisation, le nombre de pièces, la surface habitable, le code postal, etc. Les modèles sont sauvegardés au format pickle ('optimal_rfr_model.pkl' et 'optimal_linear_regression_model.pkl').

Étapes:
1. Chargement des données immobilières depuis un fichier CSV ('transactions_upload.csv').
2. Nettoyage et enrichissement des données, calcul du prix au mètre carré.
3. Filtrage des transactions immobilières en Île-de-France pour l'année 2022.
4. Sélection des caractéristiques pertinentes et calcul des sommes de surfaces.
5. Conversion des catégories en variables binaires (dummies).
6. Conversion de la date en nombre de jours depuis le 1er janvier 1970.
7. Enregistrement des données traitées dans un fichier CSV ('transactions_idf.csv').
8. Mise en place d'une API FastAPI avec deux routes pour prédire le prix au mètre carré en fonction de la géolocalisation et d'autres caractéristiques.

Modèles utilisés:
- 'optimal_rfr_model.pkl' : Modèle de Régression par Forêt aléatoire.
- 'optimal_linear_regression_model.pkl' : Modèle de Régression Linéaire.

Endpoints API:
1. `/prix_m2`: Prédiction du prix au mètre carré en fonction de la longitude et la latitude.
2. `/prix_m2_two`: Prédiction du prix au mètre carré en fonction du nombre de pièces, de la surface habitable, du prix au mètre carré, du code postal, de la longitude et la latitude.

'''


# Importation des modules nécessaires
import pickle
from fastapi import FastAPI, HTTPException
import uvicorn

# Initialisation de l'application FastAPI
app = FastAPI()

# Fonction pour charger le modèle à partir d'un fichier pickle
def load_model(file_path):
    try:
        with open(file_path, 'rb') as file:
            model = pickle.load(file)
            return model
    except FileNotFoundError:
        print('Fichier modèle introuvable')
        return None

# Fonction pour effectuer une prédiction avec deux features (n_pieces, surface_habitable, prix_m2, code_postal, longitude, latitude)
def predict_two(model, n_pieces, surface_habitable, prix_m2, code_postal, longitude, latitude):
    if model is None:
        raise HTTPException(status_code=503, detail="Modèle non chargé")
    input_data = [[n_pieces, surface_habitable, prix_m2, code_postal, longitude, latitude]]
    return model.predict(input_data)[0]

# Route pour effectuer la prédiction du prix au mètre carré en fonction de la longitude et la latitude
@app.post('/prix_m2', description="Permet de donner une prédiction du prix au mètre carré en fonction de la longitude et la latitude")
def prix_m2(longitude: float, latitude: float):
    # Chargement du modèle à chaque appel
    loaded_model = load_model('optimal_rfr_model.pkl')
    
    # Vérification du chargement du modèle
    if loaded_model is None:
        raise HTTPException(status_code=503, detail="Modèle non chargé")

    # Prédiction
    prediction = predict(loaded_model, longitude, latitude)
    return {'predicted_prix_m2': prediction}

# Route pour effectuer la prédiction du prix au mètre carré en fonction de plusieurs features
@app.post('/prix_m2_two', description="Permet de donner une prédiction du prix au mètre carré en fonction du nombre de pièces, de la surface habitable, du code postal, de la longitude et la latitude")
def prix_m2_two(n_pieces: int, surface_habitable: float, prix_m2: float, code_postal: int, longitude: float, latitude: float):
    # Chargement du modèle à chaque appel
    loaded_model = load_model('optimal_linear_regression_model.pkl')
    
    # Vérification du chargement du modèle
    if loaded_model is None:
        raise HTTPException(status_code=503, detail="Modèle non chargé")

    # Prédiction
    prediction = predict_two(loaded_model, n_pieces, surface_habitable, prix_m2, code_postal, longitude, latitude)
    
    return {'predicted_prix_m2': prediction}

# Lancement de l'application FastAPI avec le serveur uvicorn
uvicorn.run(app)