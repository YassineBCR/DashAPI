import dash
from dash import html


app = dash.Dash(__name__)

def create_bande_bleue():
    # Définir le logo
    logo = html.Img(
        src="https://cdn.discordapp.com/attachments/1186321691480166430/1199762196322861066/Design_sans_titre.png?ex=65c3b89e&is=65b1439e&hm=4db740ce8b1c743fb535f78bee908c677e6b78f64b37a70aa2e8da832ab00452",
        height="200px",  # Ajustez la hauteur de l'image à votre convenance
        width="auto",   # Réglez la largeur sur 'auto' pour maintenir le rapport hauteur/largeur
    )
# Logo
logo = html.Img(
    src='https://cdn.discordapp.com/attachments/1186321691480166430/1199762196322861066/Design_sans_titre.png?ex=65c3b89e&is=65b1439e&hm=4db740ce8b1c743fb535f78bee908c677e6b78f64b37a70aa2e8da832ab00452',
    style={
        'float': 'left',  # Positionne le logo à gauche
        'margin-right': '10px',  # Ajoute une marge à droite pour l'espace
        'width': '50px',  # Ajustez la largeur du logo selon vos besoins
        'height': '50px',  # Ajustez la hauteur du logo selon vos besoins
    }
)

# Bande bleue avec logo à gauche
bande_bleue = html.Div(
    children=[
        logo,
    ],
    style={
        'background-color': '#4285F4',
        'padding': '20px',
        'text-align': 'center',
        'width': '80%',  # Ajustez cette valeur en pourcentage ou en pixels selon vos besoins
        'margin': 'auto',  # Centre la bande_bleue horizontalement
        'height': '40px',  # Ajustez cette valeur en pixels selon vos besoins
    }
)

app.layout = html.Div(children=[bande_bleue])

if __name__ == '__main__':
    app.run_server(debug=True)
