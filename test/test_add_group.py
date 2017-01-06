# -*- coding: utf-8 -*-

from model.group import Group

# Test Create a group-------------------------------------
def test_add_group(app):  # add a fixture app as a parameter
    old_groups = app.group.get_group_list() # make a list of groups before adding a new one
    app.group.create(Group(name="My group", header="Headername", footer="Footername")) # add a new group
    new_groups = app.group.get_group_list() # make a list of groups after adding a new one
    assert len(old_groups) + 1 == len(new_groups)  # compare size of groups list after adding new group

# Test Create an empty group-------------------------------------
def test_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

