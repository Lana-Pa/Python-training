from model.group import Group

def test_add_first_contact_to_group(app):  #add a fixture app as a parameter
    # creating the new group just in case we don't have any
    app.group.create(Group(name="Group for adding contact", header="Headername", footer="Footername"))
    # add contact to the first available group
    app.contact.add_first_contact_to_group()
