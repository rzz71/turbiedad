import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px


from datetime import datetime as dt
import json
import numpy as np
import pandas as pd
import os

# Recall app
from app import app

DATA_DIR = "data"
superstore_path = os.path.join(DATA_DIR, "Base_totla.csv")

df = pd.read_csv(superstore_path,sep=";" )

##############################################################
# SCATTER PLOT
###############################################################

Scatter_fig = px.scatter(
    df,
    x="Sales",
    y="Profit",
    color="Category",
    hover_data=["State", "Sub-Category", "Order ID", "Product Name"],
)
Scatter_fig.update_layout(
    title="Sales vs. Profit in selected states", paper_bgcolor="#F8F9F9"
)


###############################################################
# LINE PLOT
###############################################################

df['Order_Month'] = pd.to_datetime(df['Fecha'].dt.to_period('M').astype(str))

ddf = ddf.groupby(["IDestacion", "Order_Month"]).sum().reset_index()

Line_fig = px.line(ddf, x="Order_Month", y="turbiedad", color="State")
Line_fig.update_layout(title="TURBIEDAD MENSUAL", paper_bgcolor="#F8F9F9")


Treemap_fig = px.treemap(
    df,
    path=["pH","oxigenoDisuelto","conductividad","T"],
    values="turbiedad",
    color_discrete_sequence=px.colors.qualitative.Dark24,
)

#################################################################################
# Here the layout for the plots to use.
#################################################################################
stats = html.Div(
    [
        # Place the different graph components here.
        dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=Line_fig, id="Line")),
                dbc.Col(dcc.Graph(figure=Scatter_fig, id="Scatter")),
            ]
        ),
        dbc.Row([dbc.Col(dcc.Graph(figure=Treemap_fig, id="Treemap"))]),
    ],
    className="ds4a-body",
)
