from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.Div([
        html.P("Having trouble setting the perfect price for your car...? No worries, \
               our car price prediction tool provides a means for finding a good selling price of your car based on the car specifications. \
               The car price predictions are based on the output of the machine learning model that we have painstakingly created."),

        html.P("If you want to try out our nifty little tool, simply fill in the car max power (BHP), select the car manufacture year, \
               the fuel type that the car uses (currently we only supports diesel and petrol) and the car brand in the form below. \
               Once done, click on the \"calculate selling price\" button and voila! A suitable selling price of the car will be shown below, \
               highlighted in blue.")
    ], style={"margin":'30px', "margin-bottom":'20px', "display":'inline-block'})
], fluid=True)