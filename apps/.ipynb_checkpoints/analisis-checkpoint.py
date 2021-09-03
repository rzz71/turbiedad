import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_admin_components as dac
import plotly.graph_objects as go
import plotly.express as px

from datetime import datetime as dt
import json
import numpy as np
import pandas as pd
import os


DATA_DIR = "data"
base_path = os.path.join(DATA_DIR, "Base_total.csv",)

df = pd.read_csv(base_path,sep=";" , parse_dates=["Fecha"])

##############################################################
# SCATTER PLOT
###############################################################

Scatter_fig = px.scatter(
    df,
    y="turbiedad",
    x="T",
    color="IDestacion",
    hover_data=["pH","PV","P"],
    labels={
           "turbiedad": "Turbiedad (NTU)",
                     "T": "Temp (C)",
                     "IDestacion": "Estaciones",
                     "PV":"Presión Vapor",
                      "P": "Precipitación",
        
    },    
  )
Scatter_fig.update_layout(
         paper_bgcolor="#F8F9F9"
)


###############################################################
# LINE PLOT
###############################################################

df['Order_Month'] = pd.to_datetime(df['Fecha'].dt.to_period('M').astype(str))

ddf = df.groupby(["IDestacion", "Order_Month"]).sum().reset_index()

Line_fig = px.line(ddf,
                   x="Order_Month",
                   y="turbiedad", 
                   color="IDestacion",
                   labels={
                         "turbiedad": "Turbiedad (NTU)",
                          "Order_Month": "Meses",
                          "IDestacion": "Estaciones"
                  },    
           )
Line_fig.update_layout(paper_bgcolor="#F8F9F9")



#################################################################################
# Here the layout for the plots to use.
#################################################################################
stats = html.Div(
    [
        # Place the different graph components here.
         dac.SimpleBox(
            	style = {'height': "600px"},
                title = "TURBIEDAD MENSUAL",
                children=[
                    dcc.Graph(figure=Line_fig,
                              id="Line",
                              config=dict(displayModeBar=False),
                              style={'width': '38vw'}
                             ),
                ],
         ),
         dac.SimpleBox(
            	style = {'height': "600px"},
                title = "Temp vs Turbiedad ",
                children=[
                     dcc.Graph(figure=Scatter_fig,
                               id="Scatter",
                              config=dict(displayModeBar=False),
                              style={'width': '38vw'}
                              )
                 ],
         ),    
    ],
        className='row',
)

analisis_tab = dac.TabItem(id='content_analisis', 
                          children= stats
                          )


