import pytest

from fixture.application import Application

@pytest.fixture(scope= "session")  #label to identify pytest fixture, one browser for all tests in session
# create fixture initialization
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy) #teardown function
    return fixture