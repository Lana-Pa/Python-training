# -*- coding: utf-8 -*-

from model.group import Group

# Test Create a group-------------------------------------
def test_add_group(app):  # add a fixture app as a parameter
    app.group.create(Group(name="My group", header="Headername", footer="Footername"))

# Test Create an empty group-------------------------------------
def test_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

