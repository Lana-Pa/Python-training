from model.contact import Contact

def test_modify_contact_first_name(app):  #add a fixture app as a parameter
    app.contact.modify_first_contact(Contact(firstname ="Edited name"))

def test_modify_contact_address(app):  #add a fixture app as a parameter
    app.contact.modify_first_contact(Contact(address ="Edited address"))