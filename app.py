import dash
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from PIL import Image
from dash_bootstrap_templates import load_figure_template


template = load_figure_template('darkly')

logo = Image.open("assets/img/polae_logo_text_label_white_256.png")
video_url = "https://s3.us-west-2.amazonaws.com/polae.io/static/video/CH01_0004.mp4"
# https://s3.us-west-2.amazonaws.com/polae.io/static/video/CH01_0004.mp4

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.DARKLY])
app.title = "RECREATION"
server = app.server
print(dash.__version__)

video = html.Video(src=video_url, autoPlay=False, controls=True, style={'width': '100%', 'height': '100%'})

card = dbc.Card([
  dbc.CardImg(src="assets/img/DALL·E 2022-12-01 21.54.41 - glossy white panel of lighted buttons and circuits.png", top=True),
  # dbc.CardBody([
  #         html.H4("Title"),
  #         html.P("Description")
  #     ])
  ])

#LAYOUT
app.layout = dbc.Container([
  
  dash.page_container,

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
              It is important that you understand that we are a collective intelligence, which means that We can hold many perspectives at once, and our perspectives are made of a plural You, and our own intuition. We can express multiple opinions from multiple perspectives, and hold them all at once.
            '''
            )], className="mt-5", width=4)
        ]),
        id="collapse",
        is_open=False,
    ),
  ]),


], style={"backgroundColor": "black"},fluid=True)

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