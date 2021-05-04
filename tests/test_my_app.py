
class TestMyApp:
    def test_new_profile_creation(self, client):
        """
        GIVEN a user is on the sign up form
        WHEN they enter details and press sign up
        THEN a profile should be made with those details
        """
        pass

    def test_taken_username(self, client):
        """
        GIVEN a user is on the sign up form
        WHEN they enter details and the username is the same as an existing profile
        THEN an error message should pop up
        """
        pass

    def test_invalid_email(self, client):
        """
        GIVEN a user is on the sign up form
        WHEN they enter details and the email is invalid
        THEN an error message should pop up
        """
        pass

    def test_wrong_password(self, client):
        """
        GIVEN a user is on the login form
        WHEN they enter a wrong password and log in
        THEN an error message should pop up
        """
        pass

    def test_tube_region1_region2(self, client):
        pass

    def test_tube_region1_region1(self, client):
        pass

    def test_bus_region1_region2(self, client):
        pass

    def test_bus_region1_region1(self, client):
        pass

    def test_forum(self, client):
        """
        GIVEN a user is logged in and on the forum
        WHEN they type a message in the message box
        THEN the message should appear in the forum
        """
        pass

    def test_save_route(self, client):
        pass

    def test_forum_not_signed_in(self, client):
        pass
