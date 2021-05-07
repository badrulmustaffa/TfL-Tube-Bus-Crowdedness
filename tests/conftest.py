# Written by Nath

import pytest
import pytest_flask
from selenium import webdriver
from selenium.webdriver import ChromeOptions

import multiprocessing
from my_app import create_app
from my_app.config import TestingConfig
from my_app.models import User


@pytest.fixture(scope="session")
def app(request):
    _app = create_app(TestingConfig)
    ctx = _app.app_context()
    ctx.push()
    yield _app
    ctx.pop()
    #pass


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()
    #pass


@pytest.fixture(scope="class")
def chrome_driver(request):
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    #options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    chrome_driver = webdriver.Chrome(options=options)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()
    #pass


@pytest.fixture(scope="class")
def run_selenium(app):
    process = multiprocessing.Process(target=app.run, args=())
    process.start()
    yield process
    process.terminate()
    #pass


@pytest.fixture(scope="function")
def user(db):
    user = User(firstname="First", lastname="Last", email="firstlast@ucl.ac.uk")
    user.set_password('password1')
    db.session.add(user)
    db.session.commit()
    return user
