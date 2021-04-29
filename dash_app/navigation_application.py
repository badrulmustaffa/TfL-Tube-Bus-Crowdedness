# Importing libraries
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash_app.layout_template import logo, nav_buttons
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

        dbc.Container(fluid=True, children=[
            # First row
            dbc.Row([
                # First column
                dbc.Col(width=4, children=[
                    html.H2('TfL Zone 1 Navigation'),
                    html.P(id="indicator"),
                    html.P("Fill in your journey information below to check the route crowdedness"),
                    dbc.Card(children=[
                        dbc.Container(
                            fluid=True, children=[
                                dbc.FormGroup([
                                    html.Br(),
                                    dbc.Toast(
                                        [dbc.Button(
                                            [html.I(className="fas fa-bus mr-2"),
                                             "BUS"]
                                            , id="bus_select", color="success",
                                            outline=False, n_clicks=0,
                                            active=True, style={'margin-right': 10}),
                                            dbc.Button(
                                                [html.I(className="fas fa-subway mr-2"),
                                                 "TRAIN"]
                                                , id="tube_select", color="success",
                                                outline=True, n_clicks=0)],
                                        header="Transportation mode:",
                                    ),

                                    dbc.Toast(
                                        [dcc.Dropdown(id='start_select',
                                                      placeholder='Search area',
                                                      value=None)],
                                        header="Start area:",
                                        icon="primary", ),

                                    dbc.Toast(
                                        [dcc.Dropdown(id='end_select',
                                                      placeholder='Search area',
                                                      value=None)],
                                        header="Destination:",
                                        icon="danger", ),

                                    html.Div(children=[
                                        dbc.Button("Clear", id="clear_button", type='reset',
                                                   color="primary", className="mr-2",
                                                   n_clicks=0),
                                        dbc.Button("Go", id="go_button",
                                                   color="primary", className="mr-2",
                                                   n_clicks=0,
                                                   external_link=True)
                                    ])
                                ])
                            ])
                    ])
                ]),

                # Second column
                dbc.Col(width=8, children=[
                    dbc.Card(children=[
                        dbc.Container(fluid=True, style={'display': 'inline-block', 'width': '100%'},
                                      id="line_figure")
                    ]),
                ]),
            ])

        ])

    ])

    init_callback(dash_app)

    return dash_app.server
