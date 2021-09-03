import dash_html_components as html
import dash_admin_components as dac
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from apps.app_plots import plot_scatter

controls = dbc.Card(
    [
    dbc.FormGroup([
            dbc.Label("pH (1-14):", width=6,),
            dbc.Col(
                dbc.Input(id="pH", type="number", min=1, max=14, value=1),
#                width=10,
                ),
            ],
            row=True,
        ),
    dbc.FormGroup([
            dbc.Label("Temperatura (5.1– 37) °C:", width=6,),
            dbc.Col(
                  dbc.Input(id="Temp", type="number", min=5.1, max=37, value=18),
                  ),
            ],
            row=True,
        ),
    dbc.FormGroup([
            dbc.Label("Presión Vapor (>0) Kpa:", width=6,),
            dbc.Col(
                  dbc.Input(id="PreVap", type="number",min=0.1, value=1),
#                width=10,
                ),
            ],
            row=True,
        ),
    dbc.FormGroup([
            dbc.Label("Precipitación mm:", width=6,),
            dbc.Col(
                  dbc.Input(id="Prec", type="number", value=0,min=0,),
                  ),
            ],
            row=True,
        ),
    dbc.Button("Predecir", color="info", className="mr-1",id="boton",n_clicks=0),
    ],
    body=True,
)



predecir_tab = dac.TabItem(id='content_predecir', 
    # Datos de entreda                          
    children=html.Div(
        [
            dac.SimpleBox(
                id="DatosEntrada",
            	style = {'height': "570px"},
                width = 4,
                children=[
                    dbc.Container(
                                  [
                                  html.H6("Ingrese los valores requeridos:"),
                                  dbc.Row(
                                         [
                                         dbc.Col(controls,md=12),
                                         ],
                                         align="center",
                                        )
                                 ]
                               )
                         ]
                    ),
            # Genrera datos de resultado
            dac.SimpleBox(
                id="Resultados",
                width = 7,
            	style = {'height': "570px"},
                children=[
                        html.Div([
                        dac.ValueBox(
                                    id="IdRMSEtrain",
                                    value="20.83 NTU",
                                    subtitle ="RMSE Train",
                                    style={'text-align':'center','font-size':'150%'},
                                    color = "primary",
                                    icon = "user",
                                    width=6
                                ),
                                dac.ValueBox(
                                  id="IdRMSEtest",
                                  elevation = 4,
                                  value = "3.49 NTU *Ultimo mes",
                                  subtitle = "RMSE Test",
                                  style={'text-align':'center','font-size':'150%'},
                                  color = "info",
                                  width=6,
                                  icon = "vial"
                                ),
                            ], className='row'),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Div([
                        dac.InfoBox(id="Idturbiedad",
                                  title = "Turbiedad",
                                  style={'background-color': '#0073b7','color':'white'}, 
                                  width = 6,  
                                  icon = "water",
                                  value="0",                                     
                                    ),
                        dac.InfoBox(id="Idcoagulante",
                                  title = "Coagulante",
                                  width = 6,
                                  style={'background-color': '#0073b7','color':'white'}, 
                                  icon = "paint-brush",
                                  value="0",
                                   ),                            
                                ], className='row'
                                ), 
                    
                        ],  className='row'
                        ),
        ], 
        className='row'
    )
)

