'''
date: 17/01/2024

Ce programme effectue les étapes suivantes:

    Chargement des données immobilières.
    Calcul du prix au mètre carré.
    Sélection des caractéristiques pertinentes.
    Transformation logarithmique de la variable cible.
    Entraînement de plusieurs modèles de régression.
    Optimisation des hyperparamètres des modèles.
    Entraînement d'un modèle d'arbre de décision et visualisation de l'arbre.
    Entraînement d'un modèle optimal de forêt aléatoire et sauvegarde du modèle.
    Visualisation des contours de décision du modèle d'arbre de décision.

'''


import pandas as pd
from matplotlib import pyplot as plt 
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor, plot_tree
import pickle from pprint import pprint


def plot_with_contour(model, X, y):
    
    # Visualisation des contours de décision
    x_min, x_max = X[:, 0].min() - 0.01, X[:, 0].max() + 0.01
    y_min, y_max = X[:, 1].min() - 0.01, X[:, 1].max() + 0.01
    
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.001),
                         np.arange(y_min, y_max, 0.001))
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=1, cmap='coolwarm')
    
    # Normalize the colormap to ignore extreme values
    # sc = plt.scatter(X[:, 0], X[:, 1], c=y, vmin=0, vmax=20_2000,
    #                 marker='o', s=5, linewidth=1, cmap='coolwarm')
    
    sc = plt.scatter(X[:, 0], X[:, 1], c=y, vmin=np.percentile(y, 5), vmax=np.percentile(y, 95), 
                     marker='o', s=5, linewidth=1, cmap='coolwarm')
    
    
    # plt.colorbar(sc, label='prix m2', orientation='vertical')
    
    
    # plt.title("Contours de décision de l'arbre de décision" )
    # plt.xlabel("Longitude")
    # plt.ylabel("Latitude")
    # plt.show()

idf_df = pd.read_csv('transactions_idf.csv')

idf_df['prix_m2'] = idf_df['prix']/(idf_df['surface_habitable'])

idf_df = idf_df[['n_pieces','surface_habitable', 'prix_m2','code_postal', 'longitude', 'latitude']]
X = idf_df[['n_pieces','surface_habitable','code_postal', 'longitude', 'latitude']].values
y = idf_df['prix_m2'].values

idf_df['prix_m2_log'] = np.log1p(idf_df['prix_m2'])
idf_df['prix_m2_log'].hist(bins=50)

X = idf_df[['n_pieces','surface_habitable','code_postal', 'longitude', 'latitude']].values
y = idf_df['prix_m2'].values

print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X.shape, y.shape)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)



m = {DecisionTreeRegressor(max_depth=100), KNeighborsRegressor(n_neighbors=50), LinearRegression(), RandomForestRegressor(max_depth=100, min_samples_leaf=10, n_estimators=1000)}

for model in m:
    model.fit(X_train, y_train)
    # plot_with_contour(model, X, y)
    print (f"modele : {model}")
    print(np.sqrt(mean_squared_error(y_train, model.predict(X_train))))
    print(np.sqrt(mean_squared_error(y_test, model.predict(X_test))))

    from sklearn.model_selection import GridSearchCV

params_grid = {
                'LR': {
                    'model': LinearRegression(),
                    'params': {
                        'fit_intercept': [True, False],
                        'positive': [True, False],
                    }
                },
                'KNR': {
                    'model': KNeighborsRegressor(),
                    'params': {
                        'n_neighbors': [10, 20, 50, 60],
                    }
                },
                'RFR': {
                    'model': RandomForestRegressor(),
                    'params': {
                        'max_depth': [50, 100, 150],
                        'min_samples_leaf': [20, 50],
                        'n_estimators': [500, 1000]

                    }
                }

            }

for model_name, model_config in params_grid.items():
    gs = GridSearchCV(estimator=model_config['model'], 
                      param_grid=model_config['params'],
                    
                      )
    gs.fit(X_train, y_train)
    print(f'Modèle: {model_name} avec params optimaux: {gs.best_params_} donne erreur =')
    print(np.sqrt(mean_squared_error(y_test, gs.best_estimator_.predict(X_test))))

model = DecisionTreeRegressor(max_depth=2)
model.fit(X, y)

plt.figure(figsize=(15, 15))
plot_tree(model, feature_names=['n_pieces','surface_habitable', 'code_postal', 'longitude', 'latitude'], fontsize=10)
plt.show()

optimal_rfr_model = RandomForestRegressor(max_depth=50, min_samples_leaf=20, n_estimators=1000)
optimal_rfr_model.fit(X_train, y_train)

pickle.dump(optimal_rfr_model, open('optimal_rfr_model_idf.pkl', 'wb'))

plt.scatter(idf_df['longitude'], idf_df['latitude'], c = idf_df.prix_m2, s=5, cmap="plasma", vmin=000, vmax=20000)
plt.title("Contours de décision de l'arbre de décision")
plt.xlabel("Longitude")
plt.ylabel("latitude")
plt.colorbar()

optimal_rfr_model = RandomForestRegressor(max_depth=50, min_samples_leaf=20, n_estimators=1000)
optimal_rfr_model.fit(X_train, y_train)

pickle.dump(optimal_rfr_model, open('optimal_rfr_model_idf.pkl', 'wb'))

from sklearn.tree import DecisionTreeRegressor, plot_tree

plt.scatter(idf_df['longitude'], idf_df['latitude'], c = idf_df.prix_m2, s=5, cmap="plasma", vmin=000, vmax=20000)
plt.title("Contours de décision de l'arbre de décision")
plt.xlabel("Longitude")
plt.ylabel("latitude")
plt.colorbar()