import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

def update_phrase():
    n=n+1
    return PHRASES[n % len(PHRASES)]


PHRASES = [
    "Welcome to our landing page!",
    "We hope you enjoy your stay.",
    "This video background is pretty cool, huh?",
    "The text in the center of the screen alternates every 5 seconds.",
    "Don't forget to check out the navbar at the top.",
    "Thanks for visiting!",
]

app.layout = html.Div([
  
  dcc.Interval(id="interval", interval=5000, n_intervals=0),
  
    # dbc.Navbar(
    #     children=[
    #         dbc.Col(html.Img(src="assets/img/polae_logo_white_256.png", height="48px"), width=2),
    #         dbc.Col(dbc.NavLink("About", href="/about", className="ml-auto"))
    #     ],
    #     color="light",
    #     light=True,
    #     dark=False,
    # ),
    html.Div(
        id="phrase-display",
        children=update_phrase(),
        style={
            "fontSize": "32px",
            "textAlign": "center",
            "position": "absolute",
            "top": "50%",
            "left": "50%",
            "transform": "translate(-50%, -50%)",
        },
    ),
    html.Div(
        id="video-background",
        children=[
            html.Video(
                src="assets/video/menagerie.mp4",
                autoPlay=True,
                loop=True,
                style={
                    "position": "fixed",
                    "top": "50%",
                    "left": "50%",
                    "minWidth": "100%",
                    "minHeight": "100%",
                    "width": "auto",
                    "height": "auto",
                    "zIndex": "-100",
                    "transform": "translate(-50%, -50%)",
                },
            )
        ],
        style={"height": "100vh"},
    ),
])


if __name__ == "__main__":
    app.run_server(debug=True)

