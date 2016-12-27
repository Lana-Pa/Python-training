from model.contact import Contact

def test_delete_first_contact(app):  #add a fixture app as a parameter
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan",
                                   middlename="Stepanovich",
                                   lastname="Ivanov",
                                   nickname="Van",
                                   title="Mr",
                                   company="Home",
                                   address="pr. Mira 55-188, Moscow, Russia",
                                   home_phone="111222555",
                                   mobile_phone="922555666",
                                   work_phone="822545654",
                                   email1="p1@co.com",
                                   email2="p2@co.com",
                                   email3="p3@co.com",
                                   homepage="www.mypage.com",
                                   address2="ul.Lenina 22-25, Moscow, Russia",
                                   phone2="456254856"))
    app.contact.delete_first_contact()
