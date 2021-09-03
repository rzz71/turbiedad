# Calls the model to calculate the turbidity

import pickle
import tpot
import pandas as pd

# load the model from disk
loaded_model = pickle.load(open('model/model_4_Variables.sav', 'rb'))

 
def calcule_turbiedad(pH, Temp, PreVap, Prec):
    """
    Calcule turbidity. Call the model (Random Forest) save whit pickle.
    
    Arguments:
    
    pH: PH
    Temp: Temperatura
    PreVap: Presion de Vapor
    Prec: Precipitacion
    
    Output:
    turbiedad: float round 4.
    """
    
    data = {'pH': pH,         ## Puede crearse 
        'T': Temp,
        'PV': PreVap,
        'P': Prec}
    input_data = pd.DataFrame(data, index = [0])
    turbiedad = loaded_model.predict(input_data.to_numpy())
    return round(turbiedad[0],4) 

def calcule_coagulante(turbiedad, pH, Temp, PreVap, Prec):
    """
    Calcule coagulante. Based in the turbidity calculate, calculate the required amount of coagulant.
    
    Arguments:
    
    turbiedad: turbiedad 
    pH: PH
    Temp: Temperatura
    PreVap: Presion de Vapor
    Prec: Precipitacion
    
    Output:
    coagulante: float round 4.
    """
    return 0

def resultados(pH,Temp,PreVap,Prec):
    """
    call funtions for calculate Turbidity and coagulante
    
    Arguments:
    
    pH: PH
    Temp: Temperatura
    PreVap: Presion de Vapor
    Prec: Precipitacion
    
    Output: The value for the box 
                str (turbidity) + NTU,
                colgulante
    """
    vTurbiedad=  str(calcule_turbiedad(pH,Temp,PreVap,Prec)) + " NTU "
    vCoagulante = calcule_coagulante(vTurbiedad, pH,Temp,PreVap, Prec)
    
    return vTurbiedad, vCoagulante 