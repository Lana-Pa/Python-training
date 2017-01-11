# -*- coding: utf-8 -*-

from model.contact import Contact


# TEST add a contact
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname ="Ivan",
                       middlename = "Stepanovich",
                       lastname = "Ivanov",
                       nickname = "Van",
                       title = "Mr",
                       company = "Home",
                       address = "pr. Mira 55-188, Moscow, Russia",
                       home_phone = "111222555",
                       mobile_phone = "922555666",
                       work_phone = "822545654",
                       email1 = "p1@co.com",
                       email2 = "p2@co.com",
                       email3 ="p3@co.com",
                       homepage = "www.mypage.com",
                       address2 = "ul.Lenina 22-25, Moscow, Russia",
                       phone2 = "456254856"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


# TEST add an empty contact
def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="",
                       middlename="",
                       lastname="",
                       nickname="",
                       title="",
                       company="",
                       address="",
                       home_phone="",
                       mobile_phone="",
                       work_phone="",
                       email1="",
                       email2="",
                       email3="",
                       homepage="",
                       address2="",
                       phone2=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
