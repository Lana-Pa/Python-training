import pytest

from fixture.application import Application

@pytest.fixture(scope= "session")  #label to identify pytest fixture, one browser for all tests in session
# create fixture initialization
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")

    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin) #teardown function
    return fixture