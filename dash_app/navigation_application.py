# Importing libraries
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash_app.navigation_layout import logo, nav_buttons, navigation_template
from dash_app.navigation_callback import init_callback

FA = "https://use.fontawesome.com/releases/v5.12.1/css/all.css"


def init_dashboard(flask_app):
    """Create a Plotly Dash dashboard"""
    dash_app = dash.Dash(server=flask_app, title='Navigation', assets_folder='../dash_app/assets',
                         routes_pathname_prefix="/navigation_dash/",
                         external_stylesheets=[dbc.themes.BOOTSTRAP, FA])

    ## Creating the app layout
    dash_app.layout = html.Div(id='page_content', children=[
        html.Header(nav_buttons()),
        html.Main(id="web_page", children=[navigation_template()]),
    ])

    init_callback(dash_app)

    return dash_app.server
