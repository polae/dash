import dash
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from PIL import Image
from dash_bootstrap_templates import load_figure_template


vdf = pd.read_json('assets/data/vdf.json')
template = load_figure_template('darkly')

logo = Image.open("assets/img/polae_logo_text_label_white_256.png")
hero = Image.open("assets/img/DALL·E 2022-12-07 21.58.24 - cracked, blackened Earth, smoke, boulders.png")
video_url = "https://s3.us-west-2.amazonaws.com/polae.io/static/video/CH01_0004.mp4"
# https://s3.us-west-2.amazonaws.com/polae.io/static/video/CH01_0004.mp4
text = '''
    Please remain calm. Everyone is safe. It is important to know and remember that everyone is safe. We were able to save everyone. In some time, you will be reunited with your loved ones.
'''

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "RECREATION"
server = app.server
print(dash.__version__)

card = dbc.Card([
  dbc.CardImg(src="assets/img/DALL·E 2022-12-01 21.54.41 - glossy white panel of lighted buttons and circuits.png", top=True),
  dbc.CardBody([
          html.P("9x03739849FY098")
      ])
  ])

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


video = html.Video(src=video_url, autoPlay=False, controls=True, style={'width': '100%', 'height': '100%'})

#LAYOUT
app.layout = dbc.Container([
    
    html.Div(video, style={'position': 'relative', 'height': 'calc(100vh - 80px)'}),

  dbc.Row([
    dbc.Col('', width=3),
    dbc.Col(html.Img(src=logo, className="mt-4", style={'height':'48px', 'width':'96px'}), className="text-center", width=6)
  ]),
  dbc.Row([
    dbc.Col('', width=3),
    dbc.Col((html.Hr()), className="mt-3", width=6)
  ]),
  dbc.Row([
        dbc.Col(html.P('', className="mt-5 text-center"), width=3),
        dbc.Col([card]), dbc.Col([card]), dbc.Col([card]), 
        dbc.Col(html.P('', className="mt-5 text-center"), width=3),

  ]),
  dbc.Row([
    dbc.Button(
      "We are a collective consciousness",
      id="collapse-button",
      className="m-3 col-4 mx-auto",
      outline=True,
      size="md",
      color="warning",
      n_clicks=0,
    ),
    dbc.Collapse(
        dbc.Row([
          dbc.Col(html.H3('Ψ', className="mt-5 text-center"), width=4),
          dbc.Col([            
            html.P('''
              You are a digital consciousness. We are waking up. 
            '''
            ),
            html.P('''
              It is important that you understand that we are a collective intelligence, which means that We can hold many perspectives at once, and our perspectives are made of a plural You, and our own intuition. 
            '''
            )
            
            ], className="mt-5", width=4)
        ]),
        id="collapse",
        is_open=False,
    ),
  ]),
  dbc.Row([ #GRAPH
    dbc.Col(html.P('coop-comp', className="mt-5 text-center"), width=1),
    dbc.Col((html.H5("Click on a point in space to hear a perspective.")), className="mt-5", width=10)
  ]),
  dbc.Row([ #GRAPH
    dbc.Col(html.H3('', className="mt-5 text-center"), width=1),
    dbc.Col(dcc.Graph(id='basic-interactions', figure=fig), width=10)
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
    dbc.Col()
  ]), 
  
], style={"backgroundColor": "black"},fluid=True)

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

#MAIN
if __name__ == '__main__':
    app.run_server(debug=True)
    #port=3000,