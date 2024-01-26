import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests

app = dash.Dash(__name__)

# Mise en page du tableau de bord
app.layout = html.Div([
    html.H1("Tableau de bord Agent"),
    
    # Saisie utilisateur pour l'année
    dcc.Input(id='year-input', type='number', value=2022, placeholder='Saisissez l\'année'),

    # Saisie utilisateur pour la ville
    dcc.Input(id='city-input', type='text', value='Montpellier', placeholder='Saisissez la ville'),

    # Actualiser le bouton
    html.Button('Actualiser', id='update-button', n_clicks=0),

    # Div pour afficher la valeur retournée
    html.Div(id='output-div')
])

# Callback pour mettre à jour la div en fonction de la saisie utilisateur
@app.callback(
    Output('output-div', 'children'),
    [Input('update-button', 'n_clicks')],
    [dash.dependencies.State('year-input', 'value'),
     dash.dependencies.State('city-input', 'value')]
)
def update_output(n_clicks, year, city):
    # Construire l'URL FastAPI en fonction de la saisie utilisateur
    fastapi_url = f"http://127.0.0.1:8000/revenu_fiscal/?year={year}&city={city}"

    # Effectuer une requête GET à l'URL FastAPI
    response = requests.get(fastapi_url)

    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        # Récupérer la valeur en retour et l'afficher
        data = response.json()
        return f"Revenu fiscal moyen pour {city} en {year}: {data}"
    else:
        # Si la requête échoue, afficher un message d'erreur
        return f"Erreur: La requête a échoué avec le code de statut {response.status_code}"

if __name__ == '__main__':
    app.run_server(debug=True)
