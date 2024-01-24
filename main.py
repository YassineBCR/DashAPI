# main.py

from dash import Dash, html, dcc, dash_table , Input, Output
import plotly.express as px
from request import revenu_fiscal_moyen

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='MDB IMMO'),

    html.Div(children='''
        Bienvenue dans ton dashboard.
    '''),
   
    dcc.Input(id='input-ville'),
    html.Div(id='div-rfm')
])

@app.callback(Output('div-rfm', 'children'),
              Input('input-ville', 'value'))

def Uptadate_rfm(city):
    return html.Div(children=str (revenu_fiscal_moyen(city=city, year=2018)))


if __name__ == '__main__':
    app.run(debug=True)