import base64
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


def logo():
    image_filename = '../my_app/static/img/SarahSquad.png'  # replace with your own image
    encoded_image = base64.b64encode(open(image_filename, 'rb').read())
    return encoded_image


def nav_buttons():
    nav_buttons = html.Div(className="navbar-collapse",
                           children=[
                               html.Ul(className="navbar-nav", children=[
                                   html.Li(className="nav-item", children=[
                                       html.A(className="nav-link", href="/",
                                              children="Home")
                                   ]),
                                   html.Li(className="nav-item", children=[
                                       html.A(className="nav-link", href="/community",
                                              children="Forum")
                                   ]),
                                   html.Li(className="nav-item", children=[
                                       html.A(className="nav-link", href="/navigation_dash/",
                                              children="Dashboard")
                                   ]),
                                   html.Li(className="nav-item", children=[
                                       html.A(className="nav-link", href="/login",
                                              children="Login")
                                   ]),
                                   html.Li(className="nav-item", children=[
                                       html.A(className="nav-link", href="/signup",
                                              children="Sign up")
                                   ]),
                               ]),
                               html.Form(className="d-flex", action="/community/display_profiles", method="post",
                                         children=[
                                             dbc.Input(className="form-control me-2", type="search",
                                                       placeholder="Type in username",
                                                       name="search_term"),
                                             html.Button(className="btn btn-outline-success", type="submit",
                                                         style={'margin-left': 8}, children="Search")

                                         ])
                           ])
    return nav_buttons


# def navbar():
#     return html.Nav(className="navbar navbar-expand-lg navbar-light bg-light",
#                     children=[
#                         html.Div(className="container-fluid", children=[
#                             html.Img(src='data:image/png;base64,{}'.format(logo().decode()),
#                                      width=50, style={'margin-right': 10, 'margin-left': -19},
#                                      className='img-thumbnail'),
#                             html.A(dbc.NavbarBrand("Sander Squad", href="/", external_link=True)),
#                             # html.Button(className="navbar-toggler", type="button",
#                             #             children=[html.Span(className="navbar-toggler-icon"),
#                             #                       dbc.Collapse(nav_buttons, id="navbar-collapse", navbar=True)
#                             #                       ]),
#                             dbc.NavbarToggler(id="navbar-toggler"),
#                             dbc.Collapse(id="navbar-collapse", navbar=True, is_open=False, children=nav_buttons()),
#                         ]),
#                     ])

    # # add callback for toggling the collapse on small screens
    # @app.callback(Output("navbar-collapse", "is_open"),
    #               [Input("navbar-toggler", "n_clicks")],
    #               [State("navbar-collapse", "is_open")])
    # def toggle_navbar_collapse(n, is_open):
    #     if n:
    #         return not is_open
    #     return is_open
