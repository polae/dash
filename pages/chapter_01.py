import dash
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc

from PIL import Image
from dash_bootstrap_templates import load_figure_template


dash.register_page(__name__)


logo = Image.open("assets/img/polae_logo_text_label_white_256.png")

# https://s3.us-west-2.amazonaws.com/polae.io/static/video/CH01_0004.mp4
text = '''
    Please remain calm. Everyone is safe. It is important to know and remember that everyone is safe. We were able to save everyone. In some time, you will be reunited with your loved ones.
'''

#LAYOUT
layout = html.Div(
  html.Img(logo)
)


