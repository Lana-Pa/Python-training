from model.contact import Contact
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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
        # wait
        element = WebDriverWait(wd, 3).until(
            EC.presence_of_element_located((By.ID, "nav")))
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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_address_book()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        # wait
        element = WebDriverWait(wd, 3).until(
            EC.presence_of_element_located((By.ID, "nav")))
        self.contact_cache = None

    def select_contact_by_id(self,contact_id):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='%s']" % contact_id).click()

    def select_group_to_add_by_id(self,group_id):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % group_id).click()

    def select_group_to_see_by_id(self,group_id):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='group']/option[@value='%s']" % group_id).click()


    def click_first_edit_button(self):
        self.click_edit_button_by_index(0)

    def click_edit_button_by_index(self, index):
        wd = self.app.wd
        self.open_address_book()
        wd.find_elements_by_xpath("//a/img[@title='Edit']")[index].click()

    def click_edit_button_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()

    def click_details_button_by_index(self, index):
        wd = self.app.wd
        self.open_address_book()
        wd.find_elements_by_xpath("//a/img[@title='Details']")[index].click()

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

    def modify_contact_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_address_book()
        self.click_edit_button_by_id(id)
        self.fill_contact_form(new_group_data)
        # submit contact edition
        wd.find_element_by_xpath("//input[@value='Update']").click()
        # wait
        element = WebDriverWait(wd, 3).until(
            EC.presence_of_element_located((By.ID, "nav")))
        self.contact_cache = None  # сброс кэша


    def open_contact_details_by_index(self, index):
        wd = self.app.wd
        self.open_address_book()
        self.click_details_button_by_index(index)
        self.contact_cache = None  # сброс кэша

    def add_contact_to_group_by_id(self, contact_id, group_id):
        wd = self.app.wd
        self.open_address_book()
        self.select_contact_by_id(contact_id)
        self.select_group_to_add_by_id(group_id)
        wd.find_element_by_xpath("//input[@value='Add to']").click()
        wd.find_element_by_xpath("//a[@href=contains(text(),'group page')]").click()
        # wait
        element = WebDriverWait(wd, 3).until(
            EC.presence_of_element_located((By.ID, "nav")))
        self.contact_cache = None

    def delete_contact_from_group_by_id(self, contact_id, group_id):
        wd = self.app.wd
        self.open_address_book()
        self.select_group_to_see_by_id(group_id)
        element = WebDriverWait(wd, 10)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_xpath("//input[@name='remove']").click()
        element = WebDriverWait(wd, 3)
        self.contact_cache = None


    # count all contacts (also a hash-function to compare lists)
    def count(self):
        wd = self.app.wd
        self.open_address_book()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):  # get info from home page
        if self.contact_cache is None:  # if cash is None, than create
            wd = self.app.wd
            self.open_address_book()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                first_name = element.find_element_by_xpath(".//td[3]").text
                last_name = element.find_element_by_xpath(".//td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                all_phones = element.find_element_by_xpath(".//td[6]").text
                all_emails = element.find_element_by_xpath(".//td[5]").text
                address = element.find_element_by_xpath(".//td[4]").text

                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page= all_emails, address=address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.click_edit_button_by_index(index)
        first_name = wd.find_element_by_name('firstname').get_attribute('value')
        last_name = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        home_phone = wd.find_element_by_name('home').get_attribute('value')
        mobile_phone = wd.find_element_by_name('mobile').get_attribute('value')
        work_phone = wd.find_element_by_name('work').get_attribute('value')
        phone2 = wd.find_element_by_name('phone2').get_attribute('value')
        email1 = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        return Contact(firstname=first_name, lastname=last_name, id=id, home_phone=home_phone,
                       mobile_phone=mobile_phone, work_phone=work_phone, phone2=phone2,
                       email1=email1, email2=email2, email3=email3, address=address)


    def get_contact_from_view_page(self,index):   # get the whole text and find only phone numbers
        wd = self.app.wd
        self.open_contact_details_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone =   re.search('H: (.*)', text).group(1)   # take only chars from group (.*)
        mobile_phone = re.search('M: (.*)', text).group(1)
        work_phone =   re.search('W: (.*)', text).group(1)
        phone2 =       re.search('P: (.*)', text).group(1)

        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, phone2=phone2)








