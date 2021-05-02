# Importing libraries
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash_app.layout import logo, nav_buttons, navigation_finder, navigation_analysis
from dash_app.callback import init_callback

FA = "https://use.fontawesome.com/releases/v5.12.1/css/all.css"


def analysis_dash(flask_app):
    """Create a Plotly Dash dashboard"""
    dash_app = dash.Dash(server=flask_app, title='Analysis', assets_folder='../dash_app/assets',
                         routes_pathname_prefix="/analysis_dash/",
                         external_stylesheets=[dbc.themes.BOOTSTRAP, FA])


    ## Creating the app layout
    dash_app.layout = html.Div(id='analysis_page', children=[
        html.Header(nav_buttons()),
        html.Main(navigation_analysis()),
    ])

    init_callback(dash_app)

    return dash_app.server
