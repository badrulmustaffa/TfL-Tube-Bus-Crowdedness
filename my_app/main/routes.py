from flask import Blueprint, render_template, redirect
# from my_app.main.functions import ConvertNavigationVariables, Graph, FindPath

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/', defaults={'name': 'traveler'})
@main_bp.route('/<name>')
def index(name):
    return redirect('/navigation_dash/')


@main_bp.route('/navigation/<mean>/<start>/<end>', methods=['GET', 'POST'])
def navigation_process(mean, start, end):
    text = "The user is requesting for {} route, from {} to {}".format(mean, start, end)
    if start == 'None':
        start = 'Bayswater'
    if end == 'None':
        end = 'Bayswater'

    # mean2, start2, end2 = ConvertNavigationVariables(mean, start, end)
    # text2 = "Equivalent to for {} route, from {} to {}".format(mean2, start2, end2)

    # Graph.dijkstra(mean2, start2, end2)
    # path = Graph.pathlist
    text2 = 'Fuck you'
    #FindPath(mean, start, end)
    return render_template('index.html', title="Navigation finder",
                           name='Bengong', message=text, message2=text2)
