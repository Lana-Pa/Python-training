import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert merge_phones_like_on_home_page(contact_from_view_page) == merge_phones_like_on_home_page(contact_from_edit_page)

    # assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    # assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    # assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    # assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!= "",  # get only non-empty rows, delete empty
                            map(lambda x: clear(x),  # apply function clear to all list elements
                                 filter(lambda x: x is not None,  # delete all empty phones
                                        [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone2]))))
