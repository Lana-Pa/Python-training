# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def create_group(self, wd, Group):
        #open group page
        wd.find_element_by_link_text("groups").click()
        #init group creation
        wd.find_element_by_name("new").click()
        #fill out form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.footer)
        wd.find_element_by_name("submit").click()
        #return to group page
        self.return_to_group(wd)

    def return_to_group(self, wd):
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    #Test Create a group-------------------------------------
    def test_add_group(self):
        wd = self.wd
        self.login(wd, username = "admin", password = "secret")
        self.create_group(wd, Group(name = "My group", header = "Headername", footer = "Footername"))
        self.logout(wd)

    # Test Create an empty group-------------------------------------
    def test_empty_group(self):
        wd = self.wd
        self.login(wd, username = "admin", password = "secret")
        self.create_group(wd, Group(name = "", header = "", footer = ""))
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

