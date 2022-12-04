import dash
from dash import Dash, html, dcc
from dash import dash_table as tbl
from dash.dash_table.Format import Group
import pandas as pd

df = pd.read_csv("assets/data_file.csv")

dash.register_page(__name__,
                   title="Data Manipulation",
                   path="/data-manipulation",
                   name="Data Manipulation")

layout = html.Div([
    html.H2("Data Manipulation"),
    html.H3("How to Work with Table"),
    html.Div("The table works with multiple operators, that can be used to filter data:"),
    tbl.DataTable(
        id="main_datatable",
        data=df.to_dict("records"),
        columns=[
            {"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns
        ],
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current=0,
        page_size=20,
    )
])