# Importing libraries
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input, State

from dash_app.layout_template import nav_buttons, logo
from dash_app.navigation_functions import AreaList, CreateBorders

FA = "https://use.fontawesome.com/releases/v5.12.1/css/all.css"


def init_dashboard(flask_app):
    """Create a Plotly Dash dashboard"""
    dash_app = dash.Dash(server=flask_app, title='Navigation', assets_folder='../dash_app/assets',
                         routes_pathname_prefix="/navigation_dash/",
                         external_stylesheets=[dbc.themes.BOOTSTRAP, FA])

    ## Creating the app layout
    dash_app.layout = html.Div(children=[
        html.Header(dbc.Navbar(className="navbar", expand='lg', light=True, color='light',
                               children=[html.Div(className="container-fluid", children=[
                                       html.Img(src='data:image/png;base64,{}'.format(logo().decode()),
                                                width=50, style={'margin-right': 10, 'margin-left': -19},
                                                className='img-thumbnail'),
                                       html.A(dbc.NavbarBrand("Sander Squad", href="/", external_link=True)),
                                       dbc.NavbarToggler(id="navbar-toggler"),
                                       dbc.Collapse([nav_buttons()], id="navbar-collapse", navbar=True),
                                   ]),
                               ])
                    ),

        dbc.Container(fluid=True, children=[
            # First row
            dbc.Row([
                # First column
                dbc.Col(width=4, children=[
                    html.H2('TfL Zone 1 Navigation'),
                    html.P("Fill in your journey information below to check the route crowdedness"),
                    dbc.Card(children=[
                        dbc.Container(
                            fluid=True, children=[
                                dbc.FormGroup([
                                    html.Br(),
                                    dbc.Toast(
                                        [dbc.Button([html.I(className="fas fa-bus mr-2"), "BUS"]
                                                    , id="bus_select", color="success", outline=False,
                                                    active=True, style={'margin-right': 10}),
                                         dbc.Button([html.I(className="fas fa-subway mr-2"), "TRAIN"]
                                                    , id="tube_select", color="success", outline=True)],
                                        header="Transportation mode:",
                                    ),

                                    dbc.Toast(
                                        [dcc.Dropdown(id='start_select', placeholder='Search area', value=None)],
                                        header="Start area:",
                                        icon="primary", ),

                                    dbc.Toast(
                                        [dcc.Dropdown(id='end_select', placeholder='Search area', value=None)],
                                        header="Destination:",
                                        icon="danger", ),

                                    html.Div(children=[
                                        dbc.Button("Clear", id="clear_button", color="primary", className="mr-2"),
                                        dbc.Button("Go", id="go_button", color="primary", className="mr-2",
                                                   external_link=True)
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
                    ]),
                ]),
            ])

        ])

    ])

    init_callback(dash_app)

    return dash_app.server


## Create callback for changing line from dropdown
def init_callback(app):
    @app.callback(
        Output("collapse", "is_open"),
        [Input("collapse-button", "n_clicks")],
        [State("collapse", "is_open")])
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

    @app.callback(Output("navbar-collapse", "is_open"),
                  [Input("navbar-toggler", "n_clicks")],
                  [State("navbar-collapse", "is_open")])
    def toggle_navbar_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

    @app.callback([Output("start_select", "options"),
                   Output("end_select", "options"),
                   Output("bus_select", "n_clicks"),
                   Output("tube_select", "n_clicks"),
                   Output("bus_select", "outline"),
                   Output("tube_select", "outline"),
                   Output("bus_select", "active"),
                   Output("tube_select", "active")],
                  [Input("bus_select", "n_clicks"),
                   Input("tube_select", "n_clicks")])
    def mean_selection(bus_n_clicks, tube_n_clicks):
        mean_select = 'Bus'
        bus_clicked = False
        tube_clicked = True
        bus_bold = True
        tube_bold = False
        if bus_n_clicks is not None:
            mean_select = 'Bus'
            bus_clicked = False
            tube_clicked = True
            bus_bold = True
            tube_bold = False
        elif tube_n_clicks is not None:
            mean_select = 'Tube'
            bus_clicked = True
            tube_clicked = False
            bus_bold = False
            tube_bold = True
        drop = [{"label": x, "value": x} for x in AreaList(mean_select)['Name']]
        return drop, drop, None, None, bus_clicked, tube_clicked, bus_bold, tube_bold

    @app.callback([Output("line_figure", "children"),
                   Output("go_button", "href")],
                  [Input("bus_select", "outline"),
                   Input("tube_select", "outline"),
                   Input("start_select", "value"),
                   Input("end_select", "value")])
    def render_figure(bus_clicked, tube_clicked, start_select, end_select):
        mean_select = 'Bus'
        if not bus_clicked:
            mean_select = 'Bus'
        if not tube_clicked:
            mean_select = 'Tube'
        fig = CreateBorders(mean_select, start_select, end_select)
        link = '/navigation/{}/{}/{}'.format(mean_select, start_select, end_select)
        return dcc.Graph(figure=fig), link

    @app.callback([Output("start_select", "value"),
                   Output("end_select", "value")],
                  [Input("clear_button", "n_clicks")])
    def clear_selection(clear_n_clicks):
        if clear_n_clicks is not None:
            return None, None
