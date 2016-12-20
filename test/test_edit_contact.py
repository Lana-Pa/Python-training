from model.contact import Contact

def test_edit_first_contact(app):  #add a fixture app as a parameter
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname ="Edited",
                       middlename = "Edited",
                       lastname = "Edited",
                       nickname = "Edited",
                       title = "Edited",
                       company = "Edited",
                       address = "Edited",
                       home_phone = "Edited",
                       mobile_phone = "Edited",
                       work_phone = "Edited",
                       email1 = "Edited",
                       email2 = "Edited",
                       email3 ="Edited",
                       homepage = "Edited",
                       address2="",
                       phone2=""))
    app.session.logout()