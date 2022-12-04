"""
This is the main page of the app
"""

import dash
from dash import Dash, Input, Output, html, dcc

dash.register_page(__name__,
                   path="/",
                   title="Home",
                   name="Home"
                   )

layout = html.Div([
    html.H2(
        "Home"
    ),

    html.H3("Information"),

    html.Div([
        "This is a web-application, that can be used to analyse data about ",
        html.U("Russian household income and spending"),
        ".",
        html.Br(),
        "The data includes 1386 Moscow-based households observed through 4th quarter of 2020.",
        html.Br(),
        "You can read more about the data ",
        dcc.Link("here", href=dash.page_registry["pages.data_description"]["path"])
        ])
])