# Importing libraries
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input, State

from dash_app.layout_template import navbar

## Creating a Dash app
from dash_app.navigation_functions import AreaList, CreateBorders


def init_dashboard(flask_app):
    """Create a Plotly Dash dashboard"""
    dash_app = dash.Dash(server=flask_app,
                         routes_pathname_prefix="/navigation_dash/",
                         external_stylesheets=[dbc.themes.BOOTSTRAP])

    ## Creating the app layout
    dash_app.layout = html.Div(children=[
        html.Header(navbar()),
        dbc.Container(fluid=True, children=[
            # First row
            dbc.Row([
                # First column
                dbc.Col(width=4, children=[
                    html.H2('Navigation'),
                    dbc.Card(children=[
                        dbc.Container(
                            fluid=True, children=[
                                dbc.FormGroup([
                                    html.Br(),
                                    html.Label(['Transportation mode:',
                                                dcc.Dropdown(id='mean_select',
                                                             options=[{"label": x, "value": x} for x in
                                                                      ['Bus', 'Tube']],
                                                             value='Bus')],
                                               style={'width': '100%', 'display': 'inline-block'}
                                               ),

                                    html.Br(),
                                    html.Label(['Start area:',
                                                dcc.Dropdown(id='start_select', placeholder='Search area', value=None)],
                                               style={'width': '100%', 'display': 'inline-block'}),

                                    html.Br(),
                                    html.Label(['Destination:',
                                                dcc.Dropdown(id='end_select', placeholder='Search area', value=None)],
                                               style={'width': '100%', 'display': 'inline-block'}),

                                    html.Br(), html.Br(),
                                    html.Div(children=[
                                        dbc.Button("Clear", id="clear_button", color="primary", className="mr-2"),
                                        dbc.Button("Go", id="go_button", color="primary", className="mr-2")
                                    ])
                                ])
                            ])
                    ])
                ]),

                # Second column
                dbc.Col(width=8, children=[
                    dbc.Card(children=[dbc.FormGroup([
                        dbc.Container(id="line_figure", fluid=True, style={'display': 'inline-block', 'width': '100%'})
                    ])
                    ])
                ]),
            ])

        ])

    ])

    init_callback(dash_app)

    return dash_app.server


## Create callback for changing line from dropdown
def init_callback(app):
    @app.callback([Output("start_select", "options"),
                   Output("end_select", "options")],
                  [Input("mean_select", "value")])
    def update_area_dropdown(mean_select):
        drop = [{"label": x, "value": x} for x in AreaList(mean_select)['Name']]
        return drop, drop

    @app.callback(Output("line_figure", "children"),
                  [Input("mean_select", "value"),
                   Input("start_select", "value"),
                   Input("end_select", "value")])
    def render_figure(mean_select, start_select, end_select):
        fig = CreateBorders(mean_select, start_select, end_select)
        return dcc.Graph(figure=fig)
