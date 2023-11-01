import pytest


try:
    class LoginTest():
        def test_login(self):
            print("login Success!")

        def test_logoff(self):
            print("Logoff Success!")

        def test_calculation(self):
            assert 2 + 2 == 4

    login = LoginTest()
    login.test_login()
    login.test_logoff()
    login.test_calculation()

except Exception as e:
    print(e)
