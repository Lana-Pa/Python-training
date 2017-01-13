from model.contact import Contact
from random import randrange

def test_delete_first_contact(app):  # add a fixture app as a parameter
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan"))
    old_contacts = app.contact.get_contact_list()

    index = index = randrange(len(old_contacts))  # generate random integer from 0 till (..)
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
