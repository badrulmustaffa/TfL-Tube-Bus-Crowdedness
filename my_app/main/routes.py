from flask import Blueprint, render_template, redirect

# from my_app.main.functions import ConvertNavigationVariables, Graph, FindPath

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/', defaults={'name': 'traveler'})
@main_bp.route('/<name>')
def index(name):
    return redirect('/navigation_dash/')


@main_bp.route('/analysis', defaults={'name': 'traveler'})
@main_bp.route('/analysis/<name>')
def analysis(name):
    return redirect('/analysis_dash/')
