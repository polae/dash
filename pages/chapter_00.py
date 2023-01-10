import dash
from dash import html, dcc, Dash, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from dash_bootstrap_templates import load_figure_template


dash.register_page(__name__, path='/')

logo = "assets/img/polae_logo_text_label_white_256.png"

# https://s3.us-west-2.amazonaws.com/polae.io/static/video/CH01_0004.mp4
text = '''
    Please remain calm. Everyone is safe. It is important to know and remember that everyone is safe. We were able to save everyone. In some time, you will be reunited with your loved ones.
'''
pages = dash.page_registry.values()

#LAYOUT
layout = html.Div([
  html.H1(text),
  # html.P(pages)
  # dcc.Link("Chapter 01", href=page['CH01'])
])


