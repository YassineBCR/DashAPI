import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests

# Liste des villes à afficher dans la dropdown
villes = ["PARIS 18", "BEAUVAIS", "MESSIMY", "VANVES", "VIGNEUX DE BRETAGNE", "VALLAURIS",
          "HENDAYE", "TOULOUSE", "VILLENEUVE-LES-BEZIERS", "CHAMBERY"]

app = dash.Dash(__name__)

# Mise en page du tableau de bord
app.layout = html.Div([
    html.H1("Tableau de bord Agent"),
    
    # Dropdown pour sélectionner la ville
    dcc.Dropdown(
        id='city-dropdown',
        options=[{'label': ville, 'value': ville} for ville in villes],
        value='PARIS 18',  # Ville par défaut
        placeholder='Sélectionnez une ville'
    ),

    # Actualiser le bouton
    html.Button('Actualiser', id='update-button', n_clicks=0),

    # Div pour afficher la valeur retournée
    html.Div(id='output-div')
])

# Callback pour mettre à jour la div en fonction de la saisie utilisateur
@app.callback(
    Output('output-div', 'children'),
    [Input('update-button', 'n_clicks')],
    [dash.dependencies.State('city-dropdown', 'value')]
)
def update_output(n_clicks, city):
    # Construire l'URL FastAPI en fonction de la saisie utilisateur
    fastapi_url = f"http://127.0.0.1:8000/transactions_sample/?city={city}&limit=10"  # Ajout du paramètre limit

    # Effectuer une requête GET à l'URL FastAPI
    response = requests.get(fastapi_url)

    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        # Récupérer la valeur en retour et l'afficher
        data = response.json()
        return f"Dix dernières transactions pour {city}: {data}"
    else:
        # Si la requête échoue, afficher un message d'erreur
        return f"Erreur: La requête a échoué avec le code de statut {response.status_code}"

if __name__ == '__main__':
    app.run_server(debug=True)
