# -*- coding: utf-8 -*-

from model.group import Group


# Test Create a group-------------------------------------
def test_add_group(app):  # add a fixture app as a parameter
    old_groups = app.group.get_group_list() # make a list of groups before adding a new one
    group = Group(name="My group", header="Headername", footer="Footername")
    app.group.create(group) # add a new group

    assert len(old_groups) + 1 == app.group.count()  # compare size of groups list with result of hash-function count()
    new_groups = app.group.get_group_list()  # make a list of groups after adding a new one
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



# Test Create an empty group-------------------------------------
# def test_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
