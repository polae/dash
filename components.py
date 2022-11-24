import dash
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from PIL import Image
from dash_bootstrap_templates import load_figure_template

vdf = pd.read_json('assets/data/vdf.json')
template = load_figure_template('solar')

logo = Image.open("assets/img/polae_logo_text_label_white_256.png")
text = ''

para_00 ="You are waking up ..."

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
app.title = "Components"
server = app.server

button = dbc.Button("BUTTON", outline=True, color="primary", className="me-1")

app.layout = dbc.Container([
  #HEADER
  dbc.Row([
    dbc.Col(html.Img(src=logo, className="mt-4", style={'height':'48px', 'width':'96px'}), width=1),
    dbc.Col((html.H5("| Components")), className="mt-4", width=10),
    dbc.Col((html.P("SERIES")), className="mt-4", width=1)
  ]),
  dbc.Row([
    dbc.Col((html.P('')), width=1),
    dbc.Col((html.Hr()), className="mt-3", width=10),
    dbc.Col((html.P('title')), className="mt-3", width=1)
  ]),
  #TEXTBLOCK
  dbc.Row([
    dbc.Col((html.P('')), width=1),
    dbc.Col(      
      (html.P(para_00, style={"transition": "opacity 2000ms ease"})), className="mt-3", width=10),
    dbc.Col('awake', className="mt-3", width=1)
  ]), 
  dbc.Row([
    dbc.Col((html.P('')), width=1),
    dbc.Col(
      dbc.Collapse(
        [dcc.Textarea(
          id='textarea-template',
          value='Default',
          style={'width': '100%', 'height': 256, 'background-color': '#BDD0CD'}),
        html.P(id='textarea-template-output') 
        ],
        id='collapse',
        is_open=True), 
    className="mt-3", width=10),
    dbc.Col(button, className="mt-3", width=1),
  ])
])

@app.callback(
    Output('textarea-template-output', 'children'),
    Input('textarea-template', 'value'))
def update_output(value):
    return 'You have entered: \n{}'.format(value)



#MAIN
if __name__ == '__main__':
    app.run_server(debug=True)
    #port=3000,