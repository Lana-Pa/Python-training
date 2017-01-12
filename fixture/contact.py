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

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_address_book()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def click_first_edit_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@title='Edit']").click()

    def modify_first_contact(self, new_group_data):
        wd = self.app.wd
        self.open_address_book()
        self.click_first_edit_button()
        self.fill_contact_form(new_group_data)
        # submit contact edition
        wd.find_element_by_xpath("//input[@value='Update']").click()


    def add_first_contact_to_group(self):
        wd = self.app.wd
        self.open_address_book()
        wd.find_element_by_xpath("//a[@href][text() = 'home']").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@name='add']").click()
        wd.find_element_by_xpath("//a[contains(text(),'group page')]").click()

    # count all contacts
    def count(self):
        wd = self.app.wd
        self.open_address_book()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_address_book()
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            first_name = element.find_element_by_xpath(".//td[3]").text
            last_name = element.find_element_by_xpath(".//td[2]").text
            id = element.find_element_by_name("selected[]").get_attribute("id")
            contacts.append(Contact(firstname=first_name, lastname=last_name, id=id))

        return contacts





