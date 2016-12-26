import pytest

from fixture.application import Application

fixture = None

@pytest.fixture  # create fixture for initialization with checking
def app():
    global fixture
    if fixture is None:  # check for fixture validness
       fixture = Application()
       fixture.session.login(username="admin", password="secret")
    else:
       if not fixture.is_valid():  # if fixture is not valid (smth wrong with the browser)
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True) # create fixture for finalization
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin) # teardown function
    return fixture