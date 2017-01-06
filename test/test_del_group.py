from model.group import Group

def test_delete_first_group(app):  #add a fixture app as a parameter
    if app.group.count() == 0:
       app.group.create(Group(name="My group"))

    old_groups = app.group.get_group_list()  # make a list of groups before deleting a one
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()  # make a list of groups after deleting a one
    assert len(old_groups) - 1 == len(new_groups)  # compare size of groups list after deleting a group