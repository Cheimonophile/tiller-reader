from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app


layout = dbc.Container(
    children=[
        load := html.Div(),
        dbc.Row(
            children=[
                dbc.Col(
                    width=3,
                    children=[
                        "Categories",
                        dcc.Loading(
                            dcc.Dropdown(
                                multi=True,
                                clearable=True,
                                placeholder="All",
                            )
                        ),
                    ],
                ),
                dbc.Col(
                    children=[
                        dbc.Row(children="Bar Graph"),
                        dbc.Row(children="Pie Chart"),
                    ],
                ),
            ]
        ),
    ]
)
