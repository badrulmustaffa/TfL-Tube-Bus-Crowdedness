import dash_core_components as dcc
from flask_login import current_user
from dash.dependencies import Output, Input, State
from dash_app.functions import AreaList, CreateBorders, CreateBordersWithPath, RenderTubeUsageGraph
from dash_app.layout import navigation_layout, analysis_layout


## Create callback for changing line from dropdown


def dash_callback(app):
    @app.callback([Output("indicator", "children"),
                   Output("third_nav", "children"),
                   Output("third_nav", "href"),
                   Output("forth_nav", "children"),
                   Output("forth_nav", "href")],
                  [Input("page_content", "id")])
    def load_navbar(input):
        """ Display navigations based on current user"""
        name = 'traveler'
        third_nav = 'Login'
        third_link = '/login'
        forth_nav = 'Sign up'
        forth_link = '/signup'
        if not current_user.is_anonymous:
            name = current_user.username
            third_nav = 'My profile'
            third_link = '/community/profile'
            forth_nav = 'Logout'
            forth_link = '/logout'
        return 'Welcome, {}!'.format(name), third_nav, third_link, forth_nav, forth_link

    @app.callback(Output("navbar-collapse", "is_open"),
                  [Input("navbar-toggler", "n_clicks")],
                  [State("navbar-collapse", "is_open")])
    def toggle_navbar_collapse(n, is_open):
        """ Collapse button for small screen size"""
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
        drop = [{"label": x, "value": x} for x in AreaList(mean_select)['Group stations']]
        return drop, drop, None, None, bus_clicked, tube_clicked, bus_bold, tube_bold

    @app.callback(Output("line_figure", "children"),
                  Output("path_memory", "data"),
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

        if end_select:
            fig, path = CreateBordersWithPath(mean_select, start_select, end_select)
        else:
            fig = CreateBorders(mean_select, start_select, end_select)
            path = [0, 1]

        return dcc.Graph(figure=fig), path

    @app.callback([Output("start_select", "value"),
                   Output("end_select", "value"),
                   Output("clear_button", "n_clicks")],
                  [Input("clear_button", "n_clicks")])
    def clear_selection(clear_n_clicks):
        if clear_n_clicks is not None:
            return None, None, None

    @app.callback(Output("search_form", "action"),
                  [Input("search_input", "value")])
    def search_profile(value):
        return '/community/display_profiles/{}'.format(value)

    @app.callback(Output("second_card", "children"),
                  [Input("page_content", "id"),
                   Input("path_memory", "data")])
    def create_analysis(input, path):
        mean_select = 'Tube'
        fig = RenderTubeUsageGraph(path)
        return dcc.Graph(figure=fig)

