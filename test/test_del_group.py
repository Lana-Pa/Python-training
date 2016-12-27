from model.group import Group

def test_delete_first_group(app):  #add a fixture app as a parameter
    if app.group.count() == 0:
       app.group.create(Group(name="My group"))

    app.group.delete_first_group()
