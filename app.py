# -*- coding: utf-8 -*-
"""
This is the file that runs the application,
It contains a header, that is showing on all other pages
"""

import dash
from dash import Dash, Input, Output, html, dcc
import dash_bootstrap_components as dbc

# App Initialization
app = Dash(__name__, title="Household Budget", use_pages=True)  # Creating an object of the dash class

# Misc
navigation_buttons = [html.Span([dcc.Link(html.Button(page["name"]), href=page["path"])]) for page in dash.page_registry.values()]

app.layout = html.Div([
    # Upper header
    html.Div(
        [
            html.H1(
                'Russian Household Income and Spending',
                style={"padding": 10}
            ),
            html.Hr()
        ],
        style={
            "textAlign": "center",
            "margin-top": -20,  # Helps to remove whitespaces
            "margin-left": -20,  # Same
            "margin-right": -20,  # Same
            "backgroundColor": "GhostWhite"}
    ),

    html.Div([*navigation_buttons],
             style={
                 "display": "flex",
                 "justify-content": "center"
             }),

    # This thing displays pages in between headers
    html.Div([dash.page_container,
              html.H3("Acknolwedgments"),
              html.Div("This page was created by: Gorlevich Daniil, Уразбаева Алина, Шаталина Ангелина, Войтенков Валентин")],
             style={"padding-left": 40,
                    "padding-right": 40}
             ),
])

if __name__ == '__main__':
    app.run(debug=True)  # Start the flask server in local mode