from flask import request, abort, render_template, redirect, url_for
from flask.views import MethodView
from flask_login import login_required, current_user
from my_app.models import Category
from my_app.forum.forms import CategoryForm
from my_app.models import db as category_db
from my_app.models import Forum
from my_app.models import db as forum_db
from my_app.forum.forms import ForumForm


class CreateView(MethodView):
    def __init__(self, decorators, template_name, form, model, db, url):
        self.decorators = decorators
        self.template_name = template_name
        self.form = form
        self.model = model
        self.db = db
        self.redirect_url = url

    def get_post_redirect_args(self, model_instance):
        raise NotImplementedError

    def create_model_instance(self, form):
        raise NotImplementedError

    def get(self, **kwargs):
        form = self.form(request.form)
        if current_user.account_type != "administrator":
            abort(401)
        return render_template(self.template_name, form=form)

    def post(self, **kwargs):
        form = self.form(request.form)
        if current_user.account_type != "administrator":
            abort(401)
        if not form.validate():
            return render_template(self.template_name, form=form)
        model_instance = self.create_model_instance(form)
        self.db.session.add(model_instance)
        self.db.session.commit()
        args = self.get_post_redirect_args(model_instance)
        return redirect(url_for(self.redirect_url, **args))


class CreateCategory(CreateView):
    def __init__(self):
        self.decorators = [login_required]
        self.template_name = "createCategory.html"
        self.form = CategoryForm
        self.model = Category
        self.db = category_db
        self.redirect_url = "category.showCategory"

    def get_post_redirect_args(self, model_instance):
        """return url_for("category.showCategory",category_slug=)"""
        return {"slug": model_instance.slug}

    def create_model_instance(self, form):
        return self.model(form.name.data)


class CreateForum(CreateView):
    def __init__(self, **kwargs):
        self.decorators = [login_required]
        self.template_name = "createForum.html"
        self.form = ForumForm
        self.model = Forum
        self.db = forum_db
        self.redirect_url = "forum.showForum"

    def get_post_redirect_args(self, model_instance):
        return {"forum_slug": model_instance.slug}

    def create_model_instance(self, form, **kwargs):
        category = Category.query.filter_by(slug=request.view_args["category_slug"]).first()
        print(request.view_args["category_slug"])
        print(category)
        if not category:
            abort(404)
        return self.model(category.id, form.name.data, form.description.data)
