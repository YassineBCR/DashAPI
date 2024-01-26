import dash
from dash import html, dcc, callback, Output, Input
from dash.exceptions import PreventUpdate
import requests
import json

# Load endpoint configuration from the JSON file
with open('endpoints.json', 'r') as file:
    endpoints_config = json.load(file)

# Define the base URL for your API
base_url = "http://127.0.0.1:8000/"

# Create Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div(children=[
    html.H1(children='Dashboard'),

    # Create a section for each endpoint
    *[
        html.Div(children=[
            html.H3(children=endpoint),
            # Create input components based on parameters_in
            *[
                dcc.Input(
                    id=f"{endpoint}_{parameter['name']}",
                    type='text',
                    value=parameter['schema'].get('default', ''),
                    placeholder=parameter['schema'].get('title', ''),
                ) for parameter in config['parameters_in']
            ],
            # Create a button to trigger the function
            html.Button(f"Run {endpoint}", id=f"{endpoint}_button", n_clicks=0),
            # Display output
            html.Div(id=f"{endpoint}_output")
        ]) for endpoint, config in endpoints_config.items()
    ]
])


# Define callback functions for each button click
for endpoint, config in endpoints_config.items():
    @app.callback(
        Output(f"{endpoint}_output", 'children'),
        [Input(f"{endpoint}_button", 'n_clicks')],
        [Input(f"{endpoint}_{parameter['name']}", 'value') for parameter in config['parameters_in']]
    )
    def update_output(n_clicks, *args):
        if n_clicks == 0:
            raise PreventUpdate
        try:
            # Prepare the API request based on the configuration
            api_url = f"{base_url}{config['path']}"
            params = {parameter['name']: arg for parameter, arg in zip(config['parameters_in'], args)}
            response = requests.get(api_url, params=params)
            # Process the response and return the result
            result = response.json()
            return f"Result: {result}"
        except Exception as e:
            return f"Error: {str(e)}"


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
