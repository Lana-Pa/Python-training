# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

# generate random string---------------------------------------------------------------------
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# generate test data

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", home_phone="", mobile_phone="",work_phone="", email1="",email2="", email3="",
                    homepage="", address2="", phone2="")]+[
            Contact(firstname=random_string("firstname",10), middlename=random_string("middlename",10),
                    lastname=random_string("lastname",10), nickname=random_string("nickname",10),
                    title=random_string("title",10), company=random_string("company",10),
                    address=random_string("address",15), home_phone=random_string("homephone",10),
                    mobile_phone=random_string("mobilephone",10),work_phone=random_string("workphone",10),
                    email1=random_string("email1",10),email2=random_string("email2",10),
                    email3=random_string("email3",10), homepage=random_string("homepage",10), address2=random_string("address2",10),
                    phone2=random_string("phone2",10))
            for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):

    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# ------TEST add an empty contact
# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="",
#                        middlename="",
#                        lastname="",
#                        nickname="",
#                        title="",
#                        company="",
#                        address="",
#                        home_phone="",
#                        mobile_phone="",
#                        work_phone="",
#                        email1="",
#                        email2="",
#                        email3="",
#                        homepage="",
#                        address2="",
#                        phone2="")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
