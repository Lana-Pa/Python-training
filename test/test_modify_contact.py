from model.contact import Contact

def test_modify_contact_first_name(app):  #add a fixture app as a parameter
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Fedorov"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Edited name", lastname="Edited lastname")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)

    # проверки

    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_modify_contact_address(app):  #add a fixture app as a parameter
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Ivan"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(address ="Edited address"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)