
def test_delete_first_contact(app):  #add a fixture app as a parameter
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()