'''
SIMPLON BRIEF-5 PHASE PREFINING

Program: b5-p1-eval-model.py

Auteur: Olivier LAVAUD
Date: 17/01/2024

Description:
Ce programme prépare et entraîne un modèle de prédiction du prix au mètre carré en utilisant des données immobilières.
Les transactions sélectionnées sont situées en Île-de-France en 2022. Les caractéristiques comprennent la géolocalisation,
le nombre de pièces, la date, le code postal, et la surface habitable.

Étapes:
1. Chargement des données.
2. Nettoyage et enrichissement.
3. Filtrage pour Île-de-France en 2022.
4. Sélection des caractéristiques et calcul des sommes de surfaces.
5. Conversion des catégories en variables binaires.
6. Conversion de la date en nombre de jours depuis 1970-01-01.
7. Enregistrement des données traitées.

'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


# Chargement: charge le dataset
df = pd.read_csv('transactions_upload.csv')

# Nettoyage: efface le(s) colonnes inutiles 
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

# Enrichissement: crée une nouvelle valeur
df['prix_m2'] = df['prix'] / (df['surface_habitable'])

# Filtre des transactions immobilières en Île-de-France en 2022
idf_df = df[(df.departement.isin([75, 77, 78, 91, 92, 93, 94, 95])) & (df.date_transaction.str.startswith('2022-'))]

# Sélection des colonnes de surface
surface_cols = [c for c in idf_df.columns if 'surface_' in c and c != 'surface_habitable']

# Calcul de la somme des surfaces pour chaque colonne et ajout des résultats dans de nouvelles colonnes
for c in surface_cols:
    idf_df[c + '_sum'] = idf_df[c].apply(lambda x: sum(eval(x)) if 'NULL' not in x else 0)

# Exclusion des lignes où la somme des surfaces est égale à zéro
idf_df = idf_df[idf_df[surface_cols].sum(axis=1) != 0]

# Convertit les colonnes catégorielles en variables binaires (dummies)
idf_df = pd.get_dummies(idf_df, columns=['type_batiment'], dtype=int)

# Convertit la colonne 'date_transaction' en format datetime
idf_df['date_transaction'] = pd.to_datetime(idf_df['date_transaction'])

# Définit une référence de date au 1er janvier 1970
reference_date = pd.to_datetime('1970-01-01')

# Calcule le nombre de jours depuis l'époque (1970-01-01) pour chaque transaction
idf_df['days_since_epoch'] = (idf_df['date_transaction'] - reference_date).dt.days

# Supprime la colonne 'date_transaction' du DataFrame
idf_df = idf_df.drop('date_transaction', axis=1)

# Sélectionne les colonnes pour X et y
X = idf_df[['longitude', 'latitude','n_pieces','days_since_epoch','code_postal','surface_habitable']].values
y = idf_df['prix_m2'].values


# Stockage:   Donnees pré-traitées
idf_df.to_csv("transactions_idf.csv", index=False)

