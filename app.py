import dash
import dash_html_components as html
import dash_admin_components as dac
import dash_core_components as dcc
import json
import decimal
import pickle



from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

import  apps.calculos as calc
from apps.predecir import predecir_tab
from apps.analisis import analisis_tab
from apps.app_plots import plot_scatter



# =============================================================================
# Dash App and Flask Server
# =============================================================================
app = dash.Dash(__name__)
server = app.server 

# =============================================================================
# Dash Admin Components
# =============================================================================
# Navbar
right_ui = dac.NavbarDropdown(
	badge_label="!",
	badge_color="danger",
	src="https://quantee.ai",
	header_text="2 Items",
	children=[
	dac.NavbarDropdownItem(
		children="message 1",
		date="today"
	),
	dac.NavbarDropdownItem(
		children="message 2",
		date="yesterday"
	),
	]
)
							  
navbar = dac.Navbar(color = "info", 
					text="", 
                    id="idNavbar"
#					children=right_ui
                   )

# Sidebar
sidebar = dac.Sidebar(
	dac.SidebarMenu(
		[
#			dac.SidebarHeader(children="Cards"),
#			dac.SidebarMenuItem(id='tab_cards', label='Basic cards', icon='box'),
			dac.SidebarMenuItem(id='tab_predecir', label='Predecir', icon='id-card'),
			dac.SidebarMenuItem(id='tab_analisis', label='Análisis Historico', icon='image'),
#			dac.SidebarHeader(children="Boxes"),
#			dac.SidebarMenuItem(id='tab_basic_boxes', label='Basic boxes', icon='desktop'),
#			dac.SidebarMenuItem(id='tab_value_boxes', label='Value/Info boxes', icon='suitcase')
		]
	),
    style={'background-color': '#4B6587'},
	title=' Aquarisc',
	skin="dark",
#	color="primary",
	brand_color="info",
	url="http://www.aquariscsat.com/",
	src=app.get_asset_url("logo1.jpg"),
	elevation=3,
	opacity=0.8
)

# Body
body = dac.Body(
    dac.TabItems([
        predecir_tab,
        analisis_tab,
    ])
)

# Controlbar
controlbar = dac.Controlbar(
    [
        html.Br(),
        html.P("Slide to change graph "),
        dcc.Slider(
            id='controlbar-slider',
            min=10,
            max=50,
            step=1,
            value=20
        )
    ],
    skin = "light"
)

# Footer
footer = dac.Footer(
	html.A(html.Img(src=app.get_asset_url("logo_DS4a.jpg")),
		href = "https://c1-web.correlation-one.com/ds4a-latam", 
#		target = "_blank", 
	),
	right_text = "TEAM 60 / 2021"
)

# almacena la infomcion para mantenerla en la session
# dcc.Store inside the app that stores the intermediate value

store= html.Div([
    dcc.Store(id='vDataVariable'),
   ])  


# =============================================================================
# App Layout
# =============================================================================


app.layout = dac.Page([navbar, sidebar, body,controlbar,  footer, store ])


# =============================================================================
# Callbacks
# =============================================================================
def activate(input_id, 
             n_predecir, n_analisis):
    
    # Depending on tab which triggered a callback, show/hide contents of app
    if input_id == 'tab_predecir' and n_predecir:
        return True, False , "Módulo de Predicción"
    elif input_id == 'tab_analisis' and n_analisis:
        return False, True , "Módulo de Historicos"
    else:
        return True, False, " " # App init
    

@app.callback([Output('content_predecir', 'active'),
               Output('content_analisis', 'active'),
               Output('idNavbar','text')],
              [Input('tab_predecir', 'n_clicks'),
                Input('tab_analisis', 'n_clicks')]
)
def display_tab(n_predecir, n_analisis):
    
    ctx = dash.callback_context # Callback context to recognize which input has been triggered

    # Get id of input which triggered callback  
    if not ctx.triggered:
        raise PreventUpdate
    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]   

    return activate(input_id, 
                    n_predecir, n_analisis)

def activatetab(input_id, 
             n_predecir, n_analisis):
    
    # Depending on tab which triggered a callback, show/hide contents of app
    if input_id == 'tab_predecir' and n_predecir:
        return True, False 
    elif input_id == 'tab_analisis' and n_analisis:
        return False, True 
    else:
        return True, False # App init

@app.callback([Output('tab_predecir', 'active'),
               Output('tab_analisis', 'active')],
               [Input('tab_predecir', 'n_clicks'),
                Input('tab_analisis', 'n_clicks')]
              )
def activate_tab(n_predecir, n_analisis):
    
    ctx = dash.callback_context # Callback context to recognize which input has been triggered

    # Get id of input which triggered callback  
    if not ctx.triggered:
        raise PreventUpdate
    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]   

    return activatetab(input_id, 
                    n_predecir, n_analisis)

# callback 
@app.callback(
#    Output('vDataVariable','data'),
     [Output('Idturbiedad','value'),
     Output('Idcoagulante','value')],
#    Output('IdRMSEtrain','value'),
#     Output('IdRMSEtest','value')],
    [
        Input("pH", "value"),
        Input("Temp", "value"),
        Input("PreVap", "value"),
        Input("Prec","value"),
        Input("boton","n_clicks"),
    ],
)
def on_button_click(pH, Temp, PreVap,Prec,n_clicks):
    if (n_clicks == 0) or (pH is None) or (Temp is None) or (PreVap is None) or (Prec is None): #(pH < 1) or (pH > 14.1) or (Temp<5.1) or (Temp>37.1) or (PreVap <=0) or (Prec < 0):
        return 0,0
    else:
        return calc.resultados(pH,Temp,PreVap,Prec)





# Update figure on slider change
#@app.callback(
#    Output('Line', 'figure'),
#    [Input('controlbar-slider', 'value')])
#def update_box_graph(value):
#    return plot_scatter(value)

# =============================================================================
# Run app    
# =============================================================================
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050", debug=False)
