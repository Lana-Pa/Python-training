# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture  #label to identify pytest fixture
# create fixture initialization
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy) #teardown function
    return fixture

#Test Create a group-------------------------------------
def test_add_group(app):  #add a fixture app as a parameter
    app.login(username="admin", password="secret")
    app.create_group(Group(name="My group", header="Headername", footer="Footername"))
    app.logout()

# Test Create an empty group-------------------------------------
def test_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

