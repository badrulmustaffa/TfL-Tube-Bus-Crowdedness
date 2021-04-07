# Importing libraries
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input

import dash_app.plotlydash_figure_data as pfd


## Creating a Dash app
def init_dashboard(flask_app):
    """Create a Plotly Dash dashboard"""
    dash_app = dash.Dash(server=flask_app,
                         routes_pathname_prefix="/plotly_dash/",
                         external_stylesheets=[dbc.themes.BOOTSTRAP])

    ## Creating the app layout
    dash_app.layout = dbc.Container(fluid=True, children=[
        html.H1('Transport for London'),
        html.H2('Zone 1 TfL tube station total annual entry and exit based on line for 2017'),

        # Adding first row
        dbc.Row([
            # First column
            dbc.Col(width=3, children=[
                html.Br(),
                dbc.FormGroup([
                    html.H3('Please select the tube line:'),
                    dcc.Dropdown(id="line_select",
                                 options=[{"label": x, "value": x}
                                          for x in list(pfd.tubeline())], value="District")
                ]),
                html.Br(),
                html.Div(id="line_busiest")
            ]),

            # Second column
            dbc.Col(width=9, children=[
                dbc.FormGroup([
                    html.Div(id="line_figure"),
                    html.P('Note:'),
                    html.Li('Bubble size corresponds to entry and exit in millions.'),
                    html.Li('Line border shows Zone 1 region as defined by TfL.')
                ])
            ]),
        ]),
    ])

    init_callback(dash_app)

    return dash_app.server


## Create callback for changing line from dropdown
def init_callback(app):
    @app.callback(Output("line_figure", "children"),
                  [Input("line_select", "value")])
    def render_figure(line_select):
        fig = pfd.createfigure(line_select)
        return dcc.Graph(figure=fig)

    ## Create callback for returning panel
    @app.callback(Output("line_busiest", "children"),
                  [Input("line_select", "value")])
    def show_highest(line_select):
        station, number = pfd.busieststation(line_select)
        panel = html.Div([
            dbc.Card(body=True, className="bg-dark text-light", children=[
                html.Br(),
                html.H5("Busiest station:", className="card-title"),
                html.H4(station, className="card-test text-light"),
                html.Br(),
                html.H5("Yearly entry and exit:", className="card-title"),
                html.H4("{:,.1f} million".format(number), className="card-test text-light"),
                html.Br()
            ])
        ])
        return panel

## Run the web app server
# if __name__ == '__main__':
#     app.run_server(debug=True)
