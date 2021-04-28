import base64
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from flask_login import current_user


def logo():
    image_filename = '../my_app/static/img/SarahSquad.png'  # replace with your own image
    encoded_image = base64.b64encode(open(image_filename, 'rb').read())
    return encoded_image


def nav_buttons(search_button):
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
                                       html.A(className="nav-link", href="/community/view_profile",
                                              children="My profile")
                                   ]),
                                   html.Li(className="nav-item", children=[
                                       html.A(className="nav-link", href="/logout",
                                              children="Logout")
                                   ]),
                               ]),
                               search_button
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
