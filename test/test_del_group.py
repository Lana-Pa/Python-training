from model.group import Group
from random import randrange

def test_delete_some_group(app):  #add a fixture app as a parameter
    if app.group.count() == 0:
       app.group.create(Group(name="test"))

    old_groups = app.group.get_group_list()  # make a list of groups before deleting a one
    index = randrange(len(old_groups))  # generate random integer from 0 till (..)
    app.group.delete_group_by_index(index)

    # проверки
    assert len(old_groups) - 1 == app.group.count()  # compare size of groups list after deleting a group
    new_groups = app.group.get_group_list()  # make a list of groups after deleting a one
    old_groups[index:index+1] = []  # delete element from this group
    assert old_groups == new_groups

