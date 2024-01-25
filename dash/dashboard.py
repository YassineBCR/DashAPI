import dash_bootstrap_components as dbc 
from dash import Dash, dcc, html, Input, Output, State
import api_client
from dash.dependencies import State
from dash_req import *
import plotly.express as px
import pickle 
import numpy as np
import joblib 
from dash import dcc



app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Mise en page de la bande bleue avec le logo
#bande_bleue_layout = create_bande_bleue()

app.layout = html.Div(style={'backgroundColor': '#282c34', 'height': '100vh'}, children=[
     #bande_bleue_layout,
   # navbar,  # Utilisez la nouvelle barre de navigation importée
    html.Div(children='''Bienvenue dans ton dashboard.''', style={'color': 'white' , 'text-align' : 'center'}),

    # Inputs généraux
    html.Div(children='''Connaitre les revenu fiscaux moyen par ville et année.''', style={'color': 'white'}),
    dcc.Input(id='input-ville', placeholder='Insérez une ville'),
    dcc.Input(id='input-annee', type='number', placeholder='Sélectionnez une année'),

    # Div pour 'revenu_fiscal_moyen'
    html.Div(id='div-rfm', style={'color': 'white'}),

    # Input pour Transaction_sample
    dcc.Input(id='input-transaction-ville', placeholder='Insérez une ville',),
    html.Div(id='div-transaction-ville', style={'color': 'white'}),

    # Inputs spécifiques à 'acquisitions'
    dcc.Input(id='input-acquisitions-ville', placeholder='Insérez une ville', className='mt-3'),
    # Div pour 'acquisitions'
    html.Div(id='div-acquisitions', style={'color': 'white'}),

    # Inputs pour PRIX AU M2
    dcc.Input(id='input-prixm2-ville', placeholder='Insérez une ville', className='mt-3'),

    # Div pour 'prix_au_metre_carre'
    html.Div(id='div-prixm2', style={'color': 'white'}),

    # input pour transactions_count_by_department
    dcc.Input(id='input-transacpardep', placeholder='Insérez une ville', className='mt-3'),
    # Div pour transactions par department
    html.Div(id='div-transacpardep', style={'color': 'white'}),

    # Div pour transactions par department
    html.Div(id='div-transacpardep', style={'color': 'white'}),

    #div et input pour count_appartments_rooms
    dcc.Input(id='input-countappartrooms', placeholder='Insérez une ville', className='mt-3'),
    html.Div(id='div-countappartrooms', style={'color': 'white'}),

    # Div pour 'prix_au_metre_carre'
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
              [Input('input-transacpardep', 'value')]) 
def update_transactions_by_department(department): 
    if not department:
        department = '75'
    ts_data = transactions_count_by_department(department=department)
    if ts_data is not None:
        return f"Nombre de transactions pour {department} : {ts_data}"
    else:
        return "Aucune donnée disponible pour les transactions."


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
