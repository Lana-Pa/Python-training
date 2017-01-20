import re

# Compare info on home page with edit page
def test_compare_info_from_homepage_and_editpage(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

# Compate phones on view page with edit page
def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert merge_phones_like_on_home_page(contact_from_view_page) == merge_phones_like_on_home_page(contact_from_edit_page)

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
