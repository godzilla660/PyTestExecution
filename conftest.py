import pytest


@pytest.fixture()
def setUp():
    print("Launch browser")
    print("Login")
    print("Open Cart")
    print("Browse products")
    print("Remove Product")
    yield
    print("Logoff")
    print("Close browser")

@pytest.fixture()
def setUp2():
    print("Do XYZ")
    print("Do XYZZZZ")
    print("Do XYZZZZZZZ")
