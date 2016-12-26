from model.group import Group

def test_modify_group_name(app):  #add a fixture app as a parameter
    app.group.modify_first_group((Group(name="New group")))

def test_modify_group_header(app):  #add a fixture app as a parameter
    app.group.modify_first_group((Group(header="New header")))

def test_modify_group_footer(app):  #add a fixture app as a parameter
    app.group.modify_first_group((Group(footer="New footer")))
