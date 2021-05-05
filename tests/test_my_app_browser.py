import pytest


# Written by Nath
@pytest.mark.usefixtures("chrome_driver", "run_selenium")
class TestMyAppBrowser:
    def test_app_is_running(self, app):
        self.driver.implicitly_wait(8)
        self.driver.get("http://127.0.0.1:5000/")
        assert self.driver.current_url == "http://127.0.0.1:5000/navigation_dash/"

    def test_signup(self):
        username = "testname"
        email = "test@ucl.ac.uk"
        password = "testpass"
        password1 = "testpass"

        self.driver.get("http://127.0.0.1:5000/signup")
        self.driver.implicitly_wait(8)

        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("email").send_keys(email)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("password-repeat").send_keys(password1)
        self.driver.find_element_by_id("submit").click()
        self.driver.implicitly_wait(8)

        assert self.driver.current_url == "http://127.0.0.1:5000/"

        message = self.driver.find_element_by_class_name("list-unstyled").find_element_by_tag_name("li").text
        assert f"Welcome, {username}." in message
        #pass

    def test_login_incorrect_password(self):
        username = "testname"
        password = "wrongpass"

        self.driver.get("http://127.0.0.1:5000/login")
        self.driver.implicitly_wait(8)

        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("submit").click()
        self.driver.implicitly_wait(8)

        message = self.driver.find_element_by_class_name("errors").find_element_by_tag_name("li").text
        assert "Wrong password" in message
        #pass

    def test_user_search(self):
        username = "testname"
        self.driver.find_element_by_id("search_input").send_keys(username)
        self.driver.find_element_by_id("search_button").click()
        self.driver.implicitly_wait(8)

        message = self.driver.find_element_by_class_name("card-title").text
        assert username == message
        #pass

    def test_invalid_user_search(self):
        username = "abcdefg"
        self.driver.find_element_by_id("search_input").send_keys(username)
        self.driver.find_element_by_id("search_button").click()
        self.driver.implicitly_wait(8)

        message = self.driver.find_element_by_class_name("list-unstyled").find_element_by_tag_name("li").text == "Username not found"
        assert "Username not found" in message
        #pass
