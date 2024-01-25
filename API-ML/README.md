# Modèle de Prédiction d'un Prix au m² dans Paris (RandomForestRegressor)

## Aperçu

Ce dépôt contient les fichiers nécessaires pour mettre en œuvre un modèle de régression avec la méthode de Forêt Aléatoire (Random Forest). Le modèle a été développé en utilisant scikit-learn en Python et peut être déployé comme une FastAPI.

Les principaux fichiers du projet sont les suivants :

- **ml_RandomForestRegressor.ipynb :** Un notebook Jupyter qui présente le processus de création, d'entraînement et d'évaluation du modèle de Forêt Aléatoire.

- **app.py :** Un script Python qui utilise fastAPI pour créer une API Web simple pour effectuer des prédictions à l'aide du modèle entraîné.

- **random_forest_model.pkl :** Le modèle entraîné sauvegardé au format pickle pour une utilisation ultérieure.

## Instructions d'utilisation

1. **Entraîner le Modèle :** Si vous souhaitez réentraîner le modèle, référez-vous au notebook ml_RandomForestRegressor.ipynb pour les instructions détaillées.

2. **Déployer l'API :** Vous pouvez déployer l'API en exécutant le script app.py. Assurez-vous d'avoir les bibliothèques Python.

3. **Effectuer des Prédictions :** Une fois l'API déployée, vous pouvez envoyer des requêtes POST pour obtenir des prédictions.

    Assurez-vous d'ajuster les fonctionnalités et l'URL en fonction de votre cas d'utilisation.

## Remarques

- Ce projet est à des fins éducatives de ma formation Developpeur IA chez Simplon.co et peut nécessiter des adaptations pour s'adapter à des cas d'utilisation spécifiques.
- Assurez-vous d'avoir les dépendances nécessaires installées.

N'hésitez pas à personnaliser ce README en fonction de votre projet et de vos besoins spécifiques.

