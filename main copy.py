# main.py

from dash import Dash, html, dcc, dash_table , Input, Output
import plotly.express as px
from request import revenu_fiscal_moyen
from navbarr import navbar

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Mise en page de la navbar et du contenu principal
app.layout = html.Div(children=[
    navbar,  # Utilisez la nouvelle barre de navigation importée
    html.Div(children='''Bienvenue dans ton dashboard.'''),

    dcc.Input(id='input-ville', placeholder='Insérez une ville'),
    dcc.Input(id='input-annee', type='number', placeholder='Sélectionnez une année'),
    html.Div(id='div-rfm')
])


@app.callback(Output('div-rfm', 'children'),
              [Input('input-ville', 'value'),
               Input('input-annee', 'value')])
def Uptadate_rfm(city, year):
    # Utilisez une année par défaut si aucune année n'est spécifiée
    if not year:
        year = 2018
    
    return html.Div(children=str(revenu_fiscal_moyen(city=city, year=year)))



if __name__ == '__main__':
    app.run(debug=True)