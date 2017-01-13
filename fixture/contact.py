from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_address_book(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']"))>0):
            wd.find_element_by_xpath("//a[text()='home']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)

    def create(self, contact):
        wd = self.app.wd
        self.open_address_book()
        # initiate add contact
        wd.find_element_by_link_text("add new").click()
        # fill out form
        self.fill_contact_form(contact)
        wd.find_element_by_name("theform").click()
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_address_book()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def click_first_edit_button(self):
        self.click_edit_button_by_index(0)

    def click_edit_button_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//a/img[@title='Edit']")[index].click()

    def modify_first_contact(self, new_group_data):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_address_book()
        self.click_edit_button_by_index(index)
        self.fill_contact_form(new_group_data)
        # submit contact edition
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.contact_cache = None  # сброс кэша

    # count all contacts (also a hash-function to compare lists)
    def count(self):
        wd = self.app.wd
        self.open_address_book()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:  # if cash is None, than create
            wd = self.app.wd
            self.open_address_book()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                first_name = element.find_element_by_xpath(".//td[3]").text
                last_name = element.find_element_by_xpath(".//td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id))

        return list(self.contact_cache)





