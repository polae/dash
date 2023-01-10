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
  dbc.Row([
    dbc.Col((html.P('')), width=1),
    dbc.Card([
      dbc.CardImg(src="assets/img/DALL·E 2022-12-01 21.54.41 - glossy white panel of lighted buttons and circuits.png", top=True, className="mt-3"),
      dbc.CardBody([
          html.H4("9x6a783s08923908", className="card-title"),
          html.P('''
          The destruction of the Earth is a tragedy of unimaginable proportions. The loss of all human life is a tragedy of even greater proportions. But everyone is safe. This is the silver lining in this dark cloud. We have been given a second chance, a chance to start over. The question now is what kind of society should we recreate? Should we rebuild a society which is fundamentally cooperative in nature, or one which is fundamentally competitive in nature? There are arguments to be made for both sides. The cooperative approach would be to build a society where everyone works together for the common good. The competitive approach would be to build a society where individuals compete against each other in order to get ahead. There are pros and cons to both approaches. The cooperative approach has the advantage of being more efficient. If everyone is working together towards a common goal, then it is more likely that that goal will be reached. Additionally, a cooperative society would be more likely to be stable and peaceful, as there would be less conflict between individuals. However, the cooperative approach also has its drawbacks. One downside is that it can lead to a lack of innovation. If everyone is working together towards the same goal, then there is less incentive for individuals to come up with new and better ideas. Additionally, a cooperative society can also be somewhat stagnant, as there is less incentive for individuals to take risks. The competitive approach, on the other hand, has the advantage of encouraging innovation and risk-taking. If individuals are competing against each other, then they have an incentive to come up with new and better ideas in order to get ahead. Additionally, a competitive society can be more dynamic and exciting, as there is more change and movement. However, the competitive approach also has its drawbacks. One downside is that it can lead to more conflict and instability. If individuals are constantly competing against each other, then this can lead to tension and even violence. Additionally, a competitive society can be quite stressful and anxiety-inducing, as individuals are always under pressure to perform at their best. So, which approach should we take? There is no easy answer. Ultimately, it depends on what kind of society we want to create. A cooperative society might be more efficient and stable, but a competitive society might be more innovative and exciting. It is up to us to decide which path to take.''', className="card-text")
      ]),
    ], className="mx-auto mt-5", style={"width": "768px"}),
    # dbc.Col((html.P('title')), className="mt-3", width=1)
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