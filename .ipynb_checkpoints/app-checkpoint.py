import dash
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

vdf = pd.read_json('assets/data/vdf.json')


from PIL import Image
logo = Image.open("assets/img/polae_logo_text_label_white_256.png")
hero = Image.open("assets/img/DALL·E 2022-11-14 20.54.07 - a largecrack appears in the egg shell, with a tiny bird beak poking through.png")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

text = '''
    Please remain calm. Everyone is safe. It is important to know and remember that everyone is safe. We were able to save everyone. In some time, you will be reunited with your loved ones.
'''

server = app.server

app.layout = dbc.Container([
  dbc.Row([
    dbc.Col(html.Img(src=logo, className="mt-4", style={'height':'48px', 'width':'96px'}), width=3)
  ]),
  dbc.Row([
    html.Img(src=hero, className="rounded mx-auto d-block", style={'height':'640px', 'width':'640px'})
  ]),
  dbc.Row([
    dbc.Col(html.H3('Ψ', className="mt-5 text-center"), width=3),
    dbc.Col([
      html.P('''
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
      
      ], className="mt-5", width=6),
    # dbc.Col(html.Img(src=logo, className="mt-4", style={'height':'64px', 'width':'128px'}), width=3)

  ])
])


if __name__ == '__main__':
    app.run_server(debug=True)