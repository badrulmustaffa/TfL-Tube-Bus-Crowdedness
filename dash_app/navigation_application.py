# Importing libraries
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input, State

from dash_app import navigation_functions
from dash_app.layout_template import navbar


## Creating a Dash app
def init_dashboard(flask_app):
    """Create a Plotly Dash dashboard"""
    dash_app = dash.Dash(server=flask_app,
                         routes_pathname_prefix="/navigation_dash/",
                         external_stylesheets=[dbc.themes.BOOTSTRAP]
                         )
    ## Creating the app layout
    dash_app.layout = html.Div(children=[
        html.Header(navbar()),
        dbc.Container(fluid=True, children=[
            # First row
            dbc.Row([
                # First column
                dbc.Col(width=5, children=[
                    html.Br(),
                    html.H2('Navigation'),
                    dbc.Card(children=[
                        dbc.FormGroup([
                            dcc.Dropdown(id='mean_select',
                                         options=[{"label": 'Bus', "value": 'Bus'}, {"label": 'Tube', "value": 'Tube'}],
                                         value='Bus'),
                            dcc.Dropdown(id='start_select',
                                         options=[{"label": x, "value": x}
                                                  for x in list(navigation_functions.tubeline())],
                                         ),
                            dcc.Dropdown(id='end_select',
                                         options=[{"label": x, "value": x}
                                                  for x in list(navigation_functions.tubeline())],
                                         )
                        ])
                    ])
                ]),

                # Second column
                dbc.Col(width=7, children=[
                    dbc.FormGroup([
                        html.Div(id="line_figure")
                    ])

                ]),
            ])

        ])

    ])

    init_callback(dash_app)

    return dash_app.server


## Create callback for changing line from dropdown
def init_callback(app):
    @app.callback(Output("line_figure", "children"),
                  [Input("start_select", "value")])
    def render_figure(start_select):
        fig = navigation_functions.createfigure(start_select)
        return dcc.Graph(figure=fig)

