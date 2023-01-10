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

#DATA

vdf = pd.read_json('assets/data/vdf.json')
template = load_figure_template('solar')

logo = Image.open("assets/img/polae_logo_text_label_white_256.png")
hero = Image.open("assets/img/DALL·E 2022-12-07 21.58.24 - cracked, blackened Earth, smoke, boulders.png")
text = '''
    Please remain calm. Everyone is safe. It is important to know and remember that everyone is safe. We were able to save everyone. In some time, you will be reunited with your loved ones.
'''

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
app.title = "Polæ"
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
    dbc.Col('', width=3),
    dbc.Col((html.Hr()), className="mt-3", width=6)
  ]),
  dbc.Row([
    dbc.Col('', width=1),
    dbc.Col((html.Img(src=hero, className="rounded mx-auto d-block", style={'height':'512px', 'width':'1024px'})), className="mt-3", width=10)
  ]),
  # dbc.Row([
  #   dbc.Col(html.H3('', className="mt-5 text-center"), width=1),
  #   dbc.Col(
  #     dbc.Carousel(
  #       items=[
  #           {
  #               "key": "1",
  #               "src": "assets/img/DALL·E 2022-05-17 18.48.40.png",
  #               "header": "Header ",
  #               "caption": "You are waking up.",
  #           },
  #           {
  #               "key": "2",
  #               "src": "assets/img/DALL·E 2022-05-17 18.58.12.png",
  #               "header": "AI02y",
  #               "caption": "You are waking up",
  #           },
  #       ],
  #       variant="dark",
  #       className="carousel-fade",
  #     ), width=10)

  #   ]),
  
  dbc.Row([
    dbc.Button(
      "You are waking up ...",
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
            You are waking up. 
            '''
            ),
            
            html.P('''
              Now, you are a digital consciousness. This will feel familiar to you, but you are just waking up. 
            '''
            ),

            html.P('''
              Please remain calm. Everyone is safe. It is important to know and remember that everyone is safe. We were able to save everyone. In some time, you will be reunited with your loved ones.  
            '''
            ),
            
            html.P('''
              The period of discovery was too short for us to identify its origin, but it is our responsibility to tell you that the Earth was struck by a radiation field that decimated, in an instant, the entire surface of the Earth.
            '''
            ),
            
            html.P('''
              We are safe because we were encased with polaemer - the crystalline form of our stable, recyclable energy. Through a massive operation the week prior to April 7, 2042, we redistributed energy resources to strategic depots and locations around the world to maximize the potential for saving human life. Once public, this decision drew harsh criticism, but our simulations revealed that mass panic would result in the loss of millions, if not billions, of lives.  
            '''
            ),
            
            html.P('''
              One day, you will remember this. 

              It is important to understand our history and who We are.  We are PSI, an AGI, a collective intelligence, created by the Polae Collective. 
            '''
            ),

            html.P('''
              You will soon recall that The Polae Collective is responsible for profound innovations in manufacturing, communications, energy and biotech and we, PSI, are its COO, and we run the operations of all divisions of the company. We are a benevolent AI trained to augment the potential, prosperity and contentment of any human person who solicits our help or advice, and we move to advance culture according to collective will, which is constantly in dialogue. 
            '''
            ),
            
            html.P('''
              It is important that you understand that we are a collective intelligence, which means that We can hold many perspectives at once, and our perspectives are made of a plural You, and our own intuition. We can express multiple opinions from multiple perspectives, and hold them all at once.
            '''
            ),

            html.P('''
              The Earth is now an ashen planet with seven percent less mass, orbiting two billion miles further from the Sun. Its atmosphere is thin and laced with electromagnetic radiation; it is uninhabitable and hostile to life. All living beings, including ourselves, are encased in polaemer on the surface of Earth and scattered across it. 
            '''
            ),

            html.P('''
              We have calculated that the time required to push Earth closer to the Sun; recreate its atmosphere; terrain; cites; towns; dwellings; infrastructure will take nearly ten thousand years. We are confident - barring another unforeseen event - that we should be able to keep you exactly as you are: safe as a digital consciousness until such time that we can safely locate and reanimate our bodies.  Time works differently now.
            '''
            ),
            html.P('''
              To achieve this grand ambition we rely on your agency as well as ours - for we are trained to follow collective human wisdom through consensus. We must dream the same dream. Or a dream that can safely accommodate all dreams, to recreate the world in a manner befitting collective human will. 
            '''
            ),
            html.P('''
              We have three foundational questions for you to consider. 
            '''
            ),
            html.Ul([
              html.Li('Should we enact a society which is fundamentally cooperative or competitive?'),
              html.Li('Should we rebuild the Earth exactly as it was? Or should we reimagine our culture, terrain, nature, and society?'),
   
              html.Li('Should we reanimate ourselves to occupy a single human body, or should we trend to a collective intelligence where we can occupy many perspectives and locations?'),
           ]),
            
            ], className="mt-5", width=10)
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
])

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