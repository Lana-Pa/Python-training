
def test_delete_first_group(app):  #add a fixture app as a parameter
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()