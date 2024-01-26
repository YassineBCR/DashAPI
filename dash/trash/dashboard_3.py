import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests



app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='city-input', type='text', value=''),
    dcc.Graph(id='revenu-fiscal-graph'),
    dcc.Graph(id='transactions-sample-graph'),
    dcc.Graph(id='acquisitions-graph'),
])

@app.callback(
    Output('revenu-fiscal-graph', 'figure'),
    [Input('city-input', 'value')]
)
def update_revenu_fiscal_graph(city):
    # Faites une requête à votre API FastAPI pour obtenir les données nécessaires
    url = f"http://127.0.0.1:8000/revenu_fiscal/?year=2022&city={city}"
    response = requests.get(url)
    data = response.json()
    print(response)
    # Utilisez les données pour créer le graphique
    # ...

    # Retournez le graphique
    return {'data': [...], 'layout': {...}}

@app.callback(
    Output('transactions-sample-graph', 'figure'),
    [Input('city-input', 'value')]
)
def update_transactions_sample_graph(city):
    # Faites une requête à votre API FastAPI pour obtenir les données nécessaires
    url = f"http://127.0.0.1:8000/transactions_sample/?city={city}"
    response = requests.get(url)
    data = response.json()

    # Utilisez les données pour créer le graphique
    # ...

    # Retournez le graphique
    return {'data': [...], 'layout': {...}}

@app.callback(
    Output('acquisitions-graph', 'figure'),
    [Input('city-input', 'value')]
)
def update_acquisitions_graph(city):
    # Faites une requête à votre API FastAPI pour obtenir les données nécessaires
    url = f"http://127.0.0.1:8000/acquisitions/?city={city}"
    response = requests.get(url)
    data = response.json()

    # Utilisez les données pour créer le graphique
    # ...

    # Retournez le graphique
    return {'data': [...], 'layout': {...}}

if __name__ == '__main__':
    app.run_server(debug=True)
