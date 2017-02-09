from fixture.orm import ORMFixture
from model.contact import Contact
import re


def test_compare_info_from_homepage_and_db(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(orm.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contact_from_home_page)):
        home = contact_from_home_page[i]
        db = contact_from_db[i]
        assert home.all_phones_from_home_page == merge_phones_like_on_home_page(db)
        assert home.address == db.address
        assert home.all_emails_from_home_page == merge_emails_like_on_home_page(db)

# delete all unnecessary symbols
def clear(s):
    return re.sub("[() -]", "", s)

# merge phones from edit page like on home page
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!= "",  # get only non-empty rows, delete empty
                            map(lambda x: clear(x),  # apply function clear to all list elements
                                 filter(lambda x: x is not None,  # delete all empty phones
                                        [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!= "",  # get only non-empty rows, delete empty
                              filter(lambda x: x is not None,  # delete all empty emails
                                [contact.email1, contact.email2, contact.email3])))

