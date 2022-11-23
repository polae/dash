import dash
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from PIL import Image
from dash_bootstrap_templates import load_figure_template
import json
import statsmodels
import datetime

#DATA

vdf = pd.read_json('assets/data/vdf.json')
template = load_figure_template('solar')

logo = Image.open("assets/img/polae_logo_text_label_white_256.png")
#hero = Image.open("assets/img/DALL·E 2022-11-14 20.54.07 - a largecrack appears in the egg shell, with a tiny bird beak poking through.png")
text = '''
    Please remain calm. Everyone is safe. It is important to know and remember that everyone is safe. We were able to save everyone. In some time, you will be reunited with your loved ones.
'''

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
server = app.server

fig = px.scatter(vdf, 
        x="plotA", 
        y="plotB",
        size ="scale",
        title="Cooperative or competitive?",
        template=template,
        hover_data={'classification':True,
            'plotA': False,
            'plotB': False,
            'scale': False
            },
        labels = {
            'plotA': 'LOOK',
            'plotB': 'AROUND'
            },
        trendline='ols'
      )

fig3d = px.scatter_3d(vdf,
        title= "Semantic Nearness",
        x=vdf.plotX,
        y=vdf.plotY,
        z=vdf.plotZ,
        size=vdf.scale,
        hover_data={'classification':True,
                    'plotX': False,
                    'plotY': False,
                    'plotZ': False,
                    'scale': False
                    },
        labels = {
                  'plotX': 'LOOK',
                  'plotY': 'AROUND',
                  'plotZ': 'YOU'
                  },
        template=template,
        color='classification',
        #width=768,
        #height=768,
        color_continuous_scale=['Gold', 'Indigo']
        )
fig3d.update_layout(transition_easing="bounce-in-out")


#LAYOUT
app.layout = dbc.Container([
  dbc.Row([
    dbc.Col(html.Img(src=logo, className="mt-4", style={'height':'48px', 'width':'96px'}), width=3)
  ]),
  dbc.Row([
    dbc.Col('', width=3),
    dbc.Col((html.Hr()), className="mt-3", width=6)
  ]),
  dbc.Row([
    #html.Img(src=hero, className="rounded mx-auto d-block", style={'height':'768px', 'width':'768px'})
  ]),
  dbc.Row([
    dbc.Button(
      "Instructions ...",
      id="collapse-button",
      className="m-3 col-4 mx-auto",
      outline=True,
      size="md",
      color="primary",
      n_clicks=0,
    ),
    dbc.Collapse(
        dbc.Row([
          dbc.Col(html.H3('Ψ', className="mt-5 text-center"), width=1),
          dbc.Col([
            html.H4('''
            Type a response to the following 
            '''
            ),
            
            html.P('''
              Now, you are a digital consciousness. This will feel familiar to you, but you are just waking up. 
            '''
            )        
            ], className="mt-5", width=10)
        ]),
        id="collapse",
        is_open=False,
    ),
  ]),
  dbc.Row([ 
    dbc.Col(html.H3('Ψ', className="mt-5 text-center"), width=1),
    dbc.Col(
      dbc.Card(
        dbc.CardBody('Answer:', id='click-data', className="mt-3")
        ),
      className="mt-5", width=10)

  ]), 
  dbc.Row([
    dbc.Col(html.H3('Ψ', className="mt-5 text-center"), width=1),
    dbc.Col(dcc.Graph(figure=fig3d), className="mt-5", width=10)
  ]),
  dbc.Row([
    dbc.Col(html.H3('', className="mt-5 text-center"), width=1),
    dbc.Col(
      dcc.Upload(
          id='upload-image',
          children=html.Div([
              'Drag and Drop or ',
              html.A('Select Files')
          ]),
          style={
              'width': '100%',
              'height': '60px',
              'lineHeight': '60px',
              'borderWidth': '1px',
              'borderStyle': 'dashed',
              'borderRadius': '5px',
              'textAlign': 'center',
              'margin': '10px'
          },
          # Allow multiple files to be uploaded
          multiple=False
      )
    )
  ]),
  dbc.Row(
    html.Div(id='output-image-upload')
  ),
]),   



@app.callback(
    Output('click-data', 'children'),
    Input('basic-interactions', 'clickData'))
def display_click_data(clickData):
    clicked = list()
    clicked = clickData
    idx = int(clicked['points'][0]['pointIndex'])
    return_string = vdf.iloc[idx]['completion']
    return return_string

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

def parse_contents(contents, filename, date):
    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        html.Img(src=contents),
        html.Hr(),
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children    

#MAIN
if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
    #port=3000,