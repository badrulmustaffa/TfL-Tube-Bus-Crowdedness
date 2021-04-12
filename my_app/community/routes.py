from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from my_app import db, photos
from my_app.community.forms import ProfileForm
from my_app.models import Profile, User

community_bp = Blueprint('community_bp', __name__, url_prefix='/community')


@community_bp.route('/', defaults={'name': 'traveler'})
@login_required
def index(name):
    if not current_user.is_anonymous:
        name = current_user.username
    return render_template('index.html',
                           title='Community page',
                           message='This page is still empty',
                           name=name)


@community_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    profile = Profile.query.join(User).filter(User.id == current_user.id).first()
    if profile:
        return redirect(url_for('community_bp.display_profile', username=current_user.username))
    else:
        return redirect((url_for('community_bp.create_profile')))


@community_bp.route('/create_profile', methods=['GET', 'POST'])
@login_required
def create_profile():
    form = ProfileForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Set photo name to none if no photos attached
        filename = None
        # CHeck if form contains photo
        if 'photo' in request.files:
            # if the filename is not empty, save the the photo
            if request.files['photo'].filename != '':
                # Save to photos in my_app
                filename = photos.save(request.files['photo'])

        # Create a profile for database
        profile = Profile(photo=filename, bio=form.bio.data,
                          username=current_user.username, user_id=current_user.id)
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('community_bp.display_profile', username=profile.username))
    return render_template('profile.html', form=form)


@community_bp.route('/update_profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    # profile = Profile.Query
    profile = Profile.query.join(User).filter_by(id=current_user.id).first()
    form = ProfileForm(obj=profile) # Prepopulate

    if request.method == 'POST' and form.validate_on_submit():
        if 'photo' in request.files:
            # Update the saved photos in my_app
            filename = photos.save(request.files['photo'])
            profile.photo = filename

        # Update other detail
        # profile.username = form.username.data
        profile.bio = form.bio.data
        # profile.tubeline = form.tubeline.data.tubeline
        db.session.commit()
        return redirect(url_for('community_bp.display_profile', username=profile.username))
    return render_template('profile.html', form=form)


@community_bp.route('/display_profile', methods=['GET', 'POST'])
@community_bp.route('/display_profile/<username>', methods=['POST', 'GET'])
@login_required
def display_profile(username=None):
    results = None
    if username is None:
        if request.method == 'POST':
            term = request.form['search_term']
            if term == "":
                flash("Enter a name to search for")
                return redirect(url_for('community_bp.index'))
            results = Profile.query.filter(Profile.username.contains(term)).all()

    else:
        results = Profile.query.filter_by(username=username).all()

    if not results:
        flash("Username not found")
        return redirect(url_for('community_bp.index'))

    urls = []
    for result in results:
        if result.photo:
            url = photos.url(result.photo)
            urls.append(url)
    return render_template('profile_display.html', profiles=zip(results, urls))

