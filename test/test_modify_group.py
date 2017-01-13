from model.group import Group
from random import randrange

def test_modify_group_name(app):  #add a fixture app as a parameter
    if app.group.count() == 0:
       app.group.create(Group(name="My group"))

    old_groups = app.group.get_group_list()  # make a list of groups before modifying
    index = randrange(len(old_groups))  # generate random integer from 0 till (..)
    group = Group(name="New group")
    group.id = old_groups[index].id    # remember ID
    app.group.modify_group_by_index(index,group)

    # проверки

    assert len(old_groups) ==  app.group.count()  # compare size of groups list after modifying - it should be equal
    new_groups = app.group.get_group_list()  # make a list of groups after modifying
    old_groups[index] = group #1st element of old list should be new added group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



# def test_modify_group_header(app):  #add a fixture app as a parameter
#     if app.group.count() == 0:
#        app.group.create(Group(name="My group"))
#
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group((Group(header="New header")))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
# def test_modify_group_footer(app):  #add a fixture app as a parameter
#     if app.group.count() == 0:
#        app.group.create(Group(name="My group"))
#
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group((Group(footer="New footer")))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)