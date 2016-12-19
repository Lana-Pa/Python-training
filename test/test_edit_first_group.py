from model.group import Group

def test_edit_first_group(app):  #add a fixture app as a parameter
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group((Group(name=" EDITED", header=" EDITED", footer=" EDITED")))
    app.session.logout()