import dash
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from PIL import Image

logo = Image.open("assets/polae_logo_text_label_white_256.png")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

server = app.server


app.layout = dbc.Container([
  dbc.Row([
    dbc.Col([html.H1("HEADER", className="text-primary")])
  ]),
  dbc.Row([
    html.H2("Text"),
    html.Img(src=logo, className="m-5", style={'height':'48px', 'width':'96px'}),
    dbc.Button(
            "ENTER",
            id="enter-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        )])
])


if __name__ == '__main__':
    app.run_server(debug=True)