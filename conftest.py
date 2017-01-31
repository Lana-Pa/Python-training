import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.application import Application
from fixture.db import DbFixture

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture  # create fixture for initialization with checking
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']  # use "web" block from target.json
    if fixture is None or not fixture.is_valid():  # check for fixture validness
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    # check for preconditions before login
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture

@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"], password=db_config["password"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

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

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):  # work with fixtures started with "data.."
            testdata = load_from_module(fixture[5:]) # do not load first 5 symbols
            metafunc.parametrize(fixture, testdata, ids=[str(x)for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])  # do not load first 5 symbols
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])



def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())

