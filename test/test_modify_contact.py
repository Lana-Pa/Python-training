from model.contact import Contact
import random

def test_modify_contact_first_name(app, db, check_ui):  #add a fixture app as a parameter

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Fedorov"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, contact)

    # проверки

    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()  # make a list of groups after modifying
    assert old_contacts == new_contacts
    if check_ui:  # only do assertion when --check_ui option exists (it was added as a fixture to conftest.py)
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
