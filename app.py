import dash
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from PIL import Image
logo = Image.open("assets/polae_logo_text_label_white_256.png")
hero = Image.open("assets/DALL·E 2022-11-14 20.54.07 - a largecrack appears in the egg shell, with a tiny bird beak poking through.png")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

server = app.server

app.layout = dbc.Container([
  dbc.Row([
    dbc.Col(html.Img(src=logo, className="mt-4", style={'height':'48px', 'width':'96px'}), width=3)
  ]),
  dbc.Row([
    # html.Img(src=hero, className="rounded mx-auto d-block", style={'height':'640px', 'width':'640px'})
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
      )], className="mt-5", width=6),
    # dbc.Col(html.Img(src=logo, className="mt-4", style={'height':'64px', 'width':'128px'}), width=3)

  ])
])


if __name__ == '__main__':
    app.run_server(debug=True)