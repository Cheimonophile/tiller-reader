import dash
from dash import dcc
import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)
