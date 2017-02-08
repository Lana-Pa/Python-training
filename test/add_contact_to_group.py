from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

def test_add_contact_to_group(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    group = random.choice(orm.get_group_list())  # choose random group from list
    contact = random.choice(orm.get_contacts_not_in_group(Group(id=group.id)))  # choose random contact from list

    if len(orm.get_contacts_not_in_group(Group(id=group.id))) == 0:
        app.contact.create(Contact(firstname="Ivan"))
    if len(orm.get_group_list()) == 0:
       app.group.create(Group(name="test"))

    old_contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
    app.contact.add_contact_to_group_by_id(contact.id, group.id)

    new_contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)


