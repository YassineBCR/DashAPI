<<<<<<< HEAD
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, dash_table
import plotly.express as px

from dahs_app.nb_transaction_departement import nb_transaction_departement

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = nb_transaction_departement()

fig = px.bar(df, x="departement", y="nb")

table = dash_table.DataTable(id= 'data-table', data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    ''')
    ,
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    table
])

=======
import dash_bootstrap_components as dbc 
from dash import Dash, html, dcc, dash_table , Input, Output
from request import revenu_fiscal_moyen, acquisitions, prix_au_metre_carre, transactions_count_by_department
from asset.navbarr import create_bande_bleue

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Mise en page de la bande bleue avec le logo
bande_bleue_layout = create_bande_bleue()


# Mise en page de la navbar et du contenu principal
app.layout = html.Div(style={'backgroundColor': '#282c34', 'height': '100vh'}, children=[
     bande_bleue_layout,
   # navbar,  # Utilisez la nouvelle barre de navigation importée
    html.Div(children='''Bienvenue dans ton dashboard.''', style={'color': 'white' , 'text-align' : 'center'}),

    # Inputs généraux
    html.Div(children='''Connaitre les revenu fiscaux moyen par ville et année.''', style={'color': 'white'}),
    dcc.Input(id='input-ville', placeholder='Insérez une ville'),
    dcc.Input(id='input-annee', type='number', placeholder='Sélectionnez une année'),

    # Div pour 'revenu_fiscal_moyen'
    html.Div(id='div-rfm', style={'color': 'white'}),

    # Inputs spécifiques à 'acquisitions'
    dcc.Input(id='input-acquisitions-ville', placeholder='Insérez une ville', className='mt-3'),
    dcc.Input(id='input-acquisitions-anne', type='number', placeholder='Insérez une date'),

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

@app.callback(Output('div-acquisitions', 'children'),
              [Input('input-acquisitions-ville', 'value'),
               Input('input-acquisitions-anne', 'value')])
def update_acquisitions(city, year):
    if not year : 
        year = 2020
    acquisitions_data = acquisitions(city)
    
    if acquisitions_data is not None:
        # Vous devez adapter cette partie en fonction de la structure réelle des données retournées par la fonction acquisitions
        return f"Nombre d'acquisitions pour {city} en {year} : {acquisitions_data}"
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
>>>>>>> fb38d7eefb4a2e6926a2c9712a94919f25f557fe
if __name__ == '__main__':
    app.run(debug=True)
