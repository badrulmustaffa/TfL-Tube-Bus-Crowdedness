import pytest
import pytest_flask
from selenium import webdriver
from selenium.webdriver import ChromeOptions

import multiprocessing


@pytest.fixture(scope = "session")
def client(app):
    return app.test_client()
    #pass


@pytest.fixture(scope="class")
def chrome_driver(request):
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    chrome_driver = webdriver.Chrome(options=options)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()
    #pass


#@pytest_flask.fixture("live-server")
@pytest.fixture(scope="class")
def run_selenium(app):
    process = multiprocessing.Process(target=app.run, args=())
    process.start()
    yield process
    process.terminate()
    #pass