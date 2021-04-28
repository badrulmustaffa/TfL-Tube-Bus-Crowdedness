import base64
import dash_bootstrap_components as dbc
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
