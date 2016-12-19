# -*- coding: utf-8 -*-

from model.Contact import Contact


#TEST add a contact
def test_add_contact(app):
    app.session.login(username = "admin", password = "secret")
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
                       bday = "//div[@id='content']/form/select[1]//option[4]",
                       bmonth = "//div[@id='content']/form/select[2]//option[7]",
                       byear = "1970",
                       aday = "//div[@id='content']/form/select[3]//option[18]",
                       amonth = "//div[@id='content']/form/select[4]//option[3]",
                       ayear = "1970",
                       address2 = "ul.Lenina 22-25, Moscow, Russia",
                       phone2 = "456254856"))

    app.session.logout()

# TEST add an empty contact
def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
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
                       #can't make these fields empty
                                           bday="//div[@id='content']/form/select[1]//option[4]",
                       bmonth="//div[@id='content']/form/select[2]//option[7]",
                       byear="",
                       aday="//div[@id='content']/form/select[3]//option[18]",
                       amonth="//div[@id='content']/form/select[4]//option[3]",
                       ayear="",
                       address2="",
                       phone2=""))
    app.session.logout()