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
import io
import base64

#DATA

vdf = pd.read_json('assets/data/vdf.json')
template = load_figure_template('solar')

logo = Image.open("assets/img/polae_logo_text_label_white_256.png")
text = ''


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
server = app.server

def func_test():
  return dbc.Row(html.Div(text))


#LAYOUT
app.layout = dbc.Container([
  dbc.Row([
    dbc.Col(html.Img(src=logo, className="mt-4", style={'height':'48px', 'width':'96px'}), width=1),
    dbc.Col((html.H5("| Lab")), className="mt-4", width=10),
    dbc.Col((html.P("©Polae LLC")), className="mt-4", width=1)
  ]),
  dbc.Row([
    dbc.Col('', width=3),
    dbc.Col((html.Hr()), className="mt-3", width=6)
  ]),
  dbc.Row([
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
        multiple=True
    ),
    html.Div(id='output-image-upload'),
  ]),
  dbc.Row([
    dcc.Textarea(
    id='textarea-example',
    value='Textarea content initialized\nwith multiple lines of text',
    style={'background-color': 'light-blue', 'width': '100%', 'height': 300}, 
    className="m-3"),

    html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'}, 
    className="mt-3"),
    html.Div([
        dbc.Button(
            "SUBMIT", id="example-button", className="me-2", n_clicks=0
        ),
        html.Span(id="example-output", style={"verticalAlign": "middle"}),
    ]),

    func_test(),
    # html.Div(text)
    ], className="m-5"),


])

@app.callback(
    Output("example-output", "children"), 
    [Input("example-button", "n_clicks")]
)
def on_button_click(n):
    if n is None:
      return "Not clicked."
    else:
      return func_test()
      

def parse_contents(contents, filename, date):
  data = contents.encode("utf8").split(b";base64,")[1]
  with open(f'assets/img/{filename}', "wb") as fh:
    fh.write(base64.decodebytes(data))
  return html.Div([
      html.H5(filename),
      html.H6(datetime.datetime.fromtimestamp(date)),
      html.Img(src=contents),
      html.Hr(),
      html.Div('Raw Content'),
      html.Pre(contents[0:200] + '...', style={
          'whiteSpace': 'pre-wrap',
          'wordBreak': 'break-all'
      })
  ])

@app.callback(
    Output('textarea-example-output', 'children'),
    Input('textarea-example', 'value')
)
def update_output(value):
    text=value
    return 'You have entered: \n{}'.format(value), text

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
    app.run_server(debug=True)
    #port=3000,