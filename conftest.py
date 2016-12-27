import pytest

from fixture.application import Application

fixture = None

@pytest.fixture  # create fixture for initialization with checking
def app():
    global fixture
    if fixture is None:  # check for fixture validness
       fixture = Application()
    else:
       if not fixture.is_valid():  # if fixture is not valid (smth wrong with the browser)
            fixture = Application()

    # check for preconditions before login
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True) # create fixture for finalization
def stop(request):
    def fin():
        fixture.session.ensure_logout() #check for preconditions before logout
        fixture.destroy()
    request.addfinalizer(fin) # teardown function
    return fixture