import dash_bootstrap_components as dbc 
import requests
from dash import Dash, dcc, html, Input, Output, State , dcc 
import api_client
from dash.dependencies import State
from dash_req import *
import plotly.express as px
import numpy as np
import joblib 
from dash import dcc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(className='InputContainer', style={'height': '100vh'}, children=[
    html.Div(children='''Bienvenue dans ton dashboard.''', style={'color': 'white' , 'text-align' : 'center'}),
    html.Div(children='''Connaitre les revenu fiscaux moyen par ville et année.''', style={'color': 'white','text-align' : 'center'}),
    dcc.Input(id='input-ville', placeholder='Insérez une ville', className='mt-3'),
    dcc.Input(id='input-annee', type='number', placeholder='Sélectionnez une année'),
    html.Div(id='div-rfm', style={'color': 'white'}),
    dcc.Input(id='input-transaction-ville', placeholder='Insérez une ville',),
    html.Div(id='div-transaction-ville', style={'color': 'white'}),
    dcc.Input(id='input-acquisitions-ville', placeholder='Insérez une ville', className='mt-3'),
    html.Div(id='div-acquisitions', style={'color': 'white'}),
    dcc.Input(id='input-prixm2-ville', placeholder='Insérez une ville', className='mt-3'),
    html.Div(id='div-prixm2', style={'color': 'white'}),
    dcc.Input(id='input-transacpardep', placeholder='Insérez une ville', className='mt-3'),
    html.Button('Afficher le graphique', id='button-show-graph'),
    html.Div(id='div-transacpardep', style={'color': 'white'}),
    dcc.Input(id='input-countappartrooms', placeholder='Insérez une ville', className='mt-3'),
    html.Div(id='div-countappartrooms', style={'color': 'white'}),
    
])


@app.callback(Output('div-rfm', 'children'),
              [Input('input-ville', 'value'),
               Input('input-annee', 'value')])
def update_rfm(city, year):
    if not year:
        year = 2018
    rfm_value = revenu_fiscal_moyen(city=city, year=year)
    if rfm_value is not None : 
        return f"Revenu fiscal moyen pour {city} en {year} : {rfm_value}"
    else : 
        return "Aucune donnée disponible pour les revenus fiscaux moyens."
@app.callback(Output('div-transaction-ville', 'children'),
              [Input('input-transaction-ville', 'value')])
def update_transactions(city):
    if not city:
        city = 'PARIS'
    
    transactions_data = transactions_sample(city=city)
    
    if transactions_data is not None:
        if isinstance(transactions_data, int):
            return f"Nombre de transactions pour {city} : {transactions_data}"
        elif isinstance(transactions_data, list):
            # Assuming transactions_data is a list of lists
            transaction_list = [
                html.P([
                    f"Date: {item[1]}, "
                    f"Code postal: {item[6]}, "
                    f"Adresse: {item[7]}, "
                    f"Type: {item[8]}, "
                    f"Nombre de pièces: {item[11]}, "
                    f"Surface: {item[12]}",
                ])
                for item in transactions_data
            ]
            return transaction_list
        else:
            return "La structure des données n'est pas conforme."
    return "Aucune donnée disponible pour les transactions."





@app.callback(Output('div-acquisitions', 'children'),
              [Input('input-acquisitions-ville', 'value')])
def update_acquisitions(city):
    year = 2020
    acquisitions_data = acquisitions(city)
    
    if acquisitions_data is not None:
        # Vous devez adapter cette partie en fonction de la structure réelle des données retournées par la fonction acquisitions
        return f"Nombre d'acquisitions pour {city} en 2022 : {acquisitions_data}"
    else:
        return "Aucune donnée disponible pour les acquisitions."
@app.callback(Output('div-prixm2', 'children'),
              [Input('input-prixm2-ville', 'value')]) 
def update_prix_au_metre_carre(city):
    if not city:
        city = 'PARIS'
    prix_m2_value = prix_au_metre_carre(city=city)
    if prix_m2_value is not None:
        return f"Prix au m2 pour {city} : {prix_m2_value}"
    else:
        return "Aucune donnée disponible pour le prix au m2."

@app.callback(Output('div-transacpardep', 'children'),
              [Input('button-show-graph', 'n_clicks')],
              [State('input-transacpardep', 'value')]) 
def update_transactions_by_department(n_clicks, department): 
    if n_clicks is None:
        return html.Div()  # Ne rien afficher tant que le bouton n'a pas été cliqué
    if not department or not department.isdigit():
        return html.Div("Veuillez entrer un numéro de département valide.")
    transactions_count_by_department_url = 'http://127.0.0.1:8000/transactions_count_by_department/'
    params = {'department': department}
    response = requests.get(transactions_count_by_department_url, params=params)
    if response.ok:
        ts_data = pd.DataFrame.from_dict(response.json())
        if not ts_data.empty:
            ts_data = ts_data.loc[(ts_data[0] < 100)]
            fig = px.bar(ts_data, x=0, y=1, labels={'0':'départements','1':'ventes'})
            fig.update_traces(marker=dict(line=dict(width=0.1)))  # Ajuster la largeur de la ligne de la barre
            fig.update_layout(bargap=0.9)
            fig.update_layout(
                width=400,  # Définir la largeur du graphique
                height=300,  # Définir la hauteur du graphique
                margin=dict(autoexpand=True, l=50, r=50, t=50, b=50),  # Auto-expand et ajustement des marges
            )  # Définir les marges
            return html.Div([html.H3('Nombre de ventes par département'),
                             dcc.Graph(figure=fig)])
        else:
            return html.Div("Aucune donnée disponible.")
    else:
        return f"Erreur : {response.status_code}"


@app.callback(Output('div-countappartrooms', 'children'),
              [Input('input-countappartrooms', 'value')]) 
def update_count_app(city):
    if not city:
        city = 'PARIS'
    count_data = count_appartments_rooms(city=city)
    if count_data is not None:
        return f"Nombre de piece par appartement vendu pour {city} : {count_data} vendu en 2022"

if __name__ == '__main__':
    app.run(debug=True)
