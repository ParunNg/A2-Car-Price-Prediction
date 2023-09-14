# Import necessary libraries 
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from pages import home, old_model, new_model

# Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # Navigation Bar
    html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("HOME", href="/home")),
                dbc.NavItem(dbc.NavLink("OLD", href="/old_model")),
                dbc.NavItem(dbc.NavLink("NEW", href="/new_model")),
            ],
            brand="Car Price Prediction",
            brand_href="/home",
            color="dark",
            dark=True,
        )]), 
    html.Div(id='page-content', children=[]), 
])

# Create the callback to handle mutlipage inputs
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/home':
        return home.layout
    if pathname == '/old_model':
        return old_model.layout
    if pathname == '/new_model':
        return new_model.layout
    else: # if redirected to unknown link
        return home.layout

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)