import base64
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


def logo():
    image_filename = '../my_app/static/img/SarahSquad.png'  # replace with your own image
    encoded_image = base64.b64encode(open(image_filename, 'rb').read())
    return encoded_image


def nav_buttons():
    """ return the navbar based on the current user status"""
    search_button = html.Form(className="d-flex", id="search_form",
                              children=[
                                  dbc.Input(id='search_input', className="me-2",
                                            placeholder="Type in username"),
                                  dbc.Button("Search", id="search_button", color='success', outline=True,
                                             external_link=True, type='submit',
                                             style={'margin-left': 8})])

    nav_buttons = html.Div(className="navbar-collapse",
                           children=[
                               html.Ul(className="navbar-nav", children=[
                                   html.Li(className="nav-item", children=[
                                       html.A(className="nav-link", href="/",
                                              children="Home")
                                   ]),
                                   html.Li(className="nav-item", children=[
                                       html.A(className="nav-link", href="/forum",
                                              children="Forum")
                                   ]),
                                   html.Li(className="nav-item", children=[
                                       html.A(className="nav-link", id="third_nav")
                                   ]),
                                   html.Li(className="nav-item", children=[
                                       html.A(className="nav-link", id="forth_nav")
                                   ]),
                               ]),
                               search_button
                           ])

    full_navbar = dbc.Navbar(className="navbar", expand='lg', light=True, color='light',
                             children=[html.Div(className="container-fluid", children=[
                                 html.Img(
                                     src='data:image/png;base64,{}'.format(logo().decode()),
                                     width=50,
                                     style={'margin-right': 10, 'margin-left': -19},
                                     className='img-thumbnail'),
                                 html.A(dbc.NavbarBrand("Sander Squad", href="/",
                                                        external_link=True)),
                                 dbc.NavbarToggler(id="navbar-toggler"),
                                 dbc.Collapse(id="navbar-collapse", navbar=True,
                                              children=[nav_buttons]
                                              ),
                             ]),
                                       ])
    return full_navbar


def navigation_template():
    page = dbc.Container(fluid=True, children=[
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
    return page


def navigation_analysis():
    page = dbc.Container()
    return page
