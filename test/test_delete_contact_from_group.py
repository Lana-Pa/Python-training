from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

def test_del_contact_from_group(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    # check for existing any group
    if len(orm.get_group_list()) == 0:
       app.group.create(Group(name="test"))

    group = random.choice(orm.get_group_list())     # choose random group from list

    if len(orm.get_contacts_in_group(Group(id=group.id))) == 0:
        if len(orm.get_contacts_not_in_group(Group(id=group.id))) == 0:
            app.contact.create(Contact(firstname="Ivan"))
        contact_not_in_group = random.choice(orm.get_contacts_not_in_group(Group(id=group.id)))
        app.contact.add_contact_to_group_by_id(contact_not_in_group.id, group.id)

    old_contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
    contact_in_group = random.choice(old_contacts_in_group)  # choose random contact from list

    app.contact.delete_contact_from_group_by_id(contact_in_group.id, group.id)

    new_contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
    old_contacts_in_group.remove(contact_in_group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)

