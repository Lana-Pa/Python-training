from fixture.orm import ORMFixture
import re


def test_compare_info_from_homepage_and_db(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    for i in range(len(app.contact.get_contact_list())):
        contact_from_home_page = app.contact.get_contact_list()[i]
        contact_from_db = orm.get_contact_list()[i]
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)

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

