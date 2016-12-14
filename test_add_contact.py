# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    # define methods----------------------------------------------
    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def initiate_add_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, wd, firstname, middlename, lastname, nickname, title, company, address, home_phone,
                          mobile_phone, work_phone, email1, email2, email3, homepage, bday, bmonth, byear, aday, amonth,
                          ayear, address2, phone2):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(work_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage)
        if not wd.find_element_by_xpath(bday).is_selected():
            wd.find_element_by_xpath(bday).click()
        if not wd.find_element_by_xpath(bmonth).is_selected():
            wd.find_element_by_xpath(bmonth).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(byear)
        if not wd.find_element_by_xpath(aday).is_selected():
            wd.find_element_by_xpath(aday).click()
        if not wd.find_element_by_xpath(amonth).is_selected():
            wd.find_element_by_xpath(amonth).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(phone2)


    def submit_contact_creation(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    #TEST-------------------------
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username = "admin", password = "secret")
        self.initiate_add_contact(wd)
        self.fill_contact_form(wd,  firstname = "Ivan",
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
                                    phone2 = "456254856")
        self.submit_contact_creation(wd)
        self.logout(wd)



    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
