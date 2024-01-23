import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
from api_client import get
from Resquests_all import revenu_fiscal_moyen, dix_derniere_transactions
import plotly.express as px

racine_api = 'http://127.0.0.1:8000'

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Agent"),
    html.Label("Année:"),
    dcc.Input(id="year-input", type="text", value=""),
    html.Label("Ville:"),
    dcc.Input(id="city-input", type="text", value=""),
    html.Button("Obtenir le revenu fiscal moyen", id="submit-button", n_clicks=0),
    dash_table.DataTable(
        id='table',
        columns=[
            {'name': 'Revenu fiscal moyen', 'id': 'revenu_fiscal_moyen'}
        ],
        style_table={'height': '300px', 'overflowY': 'auto'}
    ),
    dcc.Graph(id='revenue-graph')
])


def update_table_data(year_value, city_value):
    try:
        result = revenu_fiscal_moyen(year_value, city_value)
        if result:
            data = [{'revenu_fiscal_moyen': r} for r in result]
            return data
        else:
            return []
    except Exception as e:
        print(f"Une erreur s'est produite lors de la mise à jour des données de la table : {e}")
        return []
    
    app.layout = html.Div([
    html.H1("Dashboard Agent"),
    html.Label("Année:"),
    dcc.Input(id="year-input", type="text", value=""),
    html.Label("Ville:"),
    dcc.Input(id="city-input", type="text", value=""),
    html.Button("Obtenir le revenu fiscal moyen", id="submit-button", n_clicks=0),
    dash_table.DataTable(
        id='table',
        columns=[
            {'name': 'Revenu fiscal moyen', 'id': 'revenu_fiscal_moyen'}
        ],
        style_table={'height': '300px', 'overflowY': 'auto'}
    ),
    dcc.Graph(id='revenue-graph')
])


def update_graph_data(city_value):
    try:
        result = dix_derniere_transactions(city_value)
        if result and len(result) == 10:
            figure = px.bar(x=[f"Transaction {i+1}" for i in range(10)], y=result, title='Revenu pour les 10 dernières transactions')
            return figure, 
        else:
            return {'data': [], 'layout': {}}
    except Exception as e:
        print(f"Une erreur s'est produite lors de la mise à jour des données du graphique : {e}")
        return {'data': [], 'layout': {}}


@app.callback(
    [Output("table", "data"),
     Output('revenue-graph', 'figure')],
    [Input("submit-button", "n_clicks")],
    [dash.dependencies.State("year-input", "value"),
     dash.dependencies.State("city-input", "value")]
)
def update_data_and_graph(n_clicks, year_value, city_value):
    if n_clicks > 0:
        try:
            # Utiliser city_value au lieu de result comme argument
            table_data = update_table_data(year_value, city_value)
            graph_data = update_graph_data(city_value)
            return table_data, graph_data
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return [], {'data': [], 'layout': {}}
    else:
        return [], {'data': [], 'layout': {}}

if __name__ == "__main__":
    app.run_server(debug=True)
