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

if __name__ == '__main__':
    app.run(debug=True)
