from model.group import Group

def test_modify_group_name(app):  #add a fixture app as a parameter
    if app.group.count() == 0:
       app.group.create(Group(name="My group"))

    old_groups = app.group.get_group_list()  # make a list of groups before modifying
    app.group.modify_first_group((Group(name="New group")))
    new_groups = app.group.get_group_list()  # make a list of groups after modifying
    assert len(old_groups) == len(new_groups)  # compare size of groups list after modifying - it should be equal

def test_modify_group_header(app):  #add a fixture app as a parameter
    if app.group.count() == 0:
       app.group.create(Group(name="My group"))

    old_groups = app.group.get_group_list()
    app.group.modify_first_group((Group(header="New header")))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_footer(app):  #add a fixture app as a parameter
    if app.group.count() == 0:
       app.group.create(Group(name="My group"))

    old_groups = app.group.get_group_list()
    app.group.modify_first_group((Group(footer="New footer")))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)