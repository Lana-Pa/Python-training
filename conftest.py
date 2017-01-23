import pytest
import json

from fixture.application import Application

fixture = None
target = None

@pytest.fixture  # create fixture for initialization with checking
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)

    if fixture is None or not fixture.is_valid():  # check for fixture validness
        fixture = Application(browser=browser, base_url=target["baseUrl"])

    # check for preconditions before login
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture

@pytest.fixture(scope="session", autouse=True) # create fixture for finalization
def stop(request):
    def fin():
        fixture.session.ensure_logout() #check for preconditions before logout
        fixture.destroy()
    request.addfinalizer(fin) # teardown function
    return fixture

# hook - add additional parameters to load tests from cmd
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")  # parameter, what to do, definition of the parameter
    parser.addoption("--target", action="store", default="target.json")