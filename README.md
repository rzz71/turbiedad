# Turbiedad
App proyecto grupo 60 DS4A 2021
***
Turbidity calculation from a Random Forest prediction model with 4 variables.

![Dash - Google Chrome 2021-09-01 10-57-27_Trim](https://user-images.githubusercontent.com/89497459/132022554-b6ec7974-edc8-4ee8-ad98-08bc53da7b3a.gif)


##Instructions

To get started, first clone this repo:

```
git clone https://github.com/rzz71/turbiedad.git
```

Install all the requirements:

```
pip install -r requirements.txt
```

You can now run the app:
```
python app.py
```

and visit http://127.0.0.1:8050/.

## Dependencies
- Python 3.8.5+
- Dash 1.19
- Dash Bootstrap Components 
- dash-core-components 
- dash-admin-components
- tpot
- pickle

The application is developed in dash, it uses the dash-admin-components “dac” library.
dash-admin-components was created by [Quantee](https://quantee.ai/), They have created a package on the top of Plotly Dash to simplify the implementation of dashboards and now, we share the results with you as an open-source solution!

## Code structure

```
app.py apps   --- predecir.py
              --- analisis.py
              --- calculos.py
       assets
       data
       model
```            
            




 
