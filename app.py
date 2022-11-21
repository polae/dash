import dash
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

server = app.server


app.layout = dbc.Container([
  dbc.Row([
    dbc.Col([html.H1("HEADER")])
  ]),
  dbc.Row([html.H2("Text")])
])


if __name__ == '__main__':
    app.run_server(debug=True)