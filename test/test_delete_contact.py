from model.contact import Contact


def test_delete_first_contact(app):  # add a fixture app as a parameter
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    app.contact.delete_first_contact()
