# -*- coding: utf-8 -*-
"""
This page contains descriptions of the data
"""

import dash
from dash import Dash, html, dcc
from dash import dash_table as tbl
from dash.dash_table.Format import Group
import pandas as pd

variable_df = pd.read_csv("assets/data_description.csv")

dash.register_page(__name__,
                   title="Data Description",
                   path="/data-description",
                   name="Data Description")  # Register the page in the page registry, so it is run under app.py process

layout = html.Div([
    html.H2("Data Description"),

    html.H3("Source and Observations"),

    html.Div([
        "The data was collected from the ",
        dcc.Link("Russian Study of Income and Spending of Households", href="https://obdx.gks.ru/", refresh=True),
        html.Br(),
        "Data was collected by the ",
        dcc.Link("Russian Statistical Agency", href="https://rosstat.gov.ru/", refresh=True),
        html.Br(),
        "The whole dataset, however, is too big to analyze, so we take only one city and one period",
        html.Br(),
        "Data contains information about 1386 Moscow-based households",
        html.Br(),
        "Households were studied through 4 quarter of 2020",
        html.Br(),
        "The data is cross-sectional - one observation represents one household"
    ]),

    html.H3("Variables"),

    tbl.DataTable(variable_df.to_dict('records'),
                  [{"name": i, "id": i} for i in variable_df.columns],
                  style_cell={"whiteSpace": "pre-line",
                              "textAlign": "center"})

])

