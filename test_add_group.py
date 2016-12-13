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
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_groups(self, wd):
        wd.find_element_by_link_text("groups").click()

    def init_group_creation(self, wd):
        wd.find_element_by_name("new").click()

    def fill_group_form(self, wd, Group):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.footer)

    def submit_group_creation(self, wd):
        wd.find_element_by_name("submit").click()

    def return_to_group(self, wd):
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    #Test Login and create a group-------------------------------------
    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username = "admin", password = "secret")
        self.open_groups(wd)
        self.init_group_creation(wd)
        self.fill_group_form(wd, Group(name = "My group", header = "Headername", footer = "Footername"))
        self.submit_group_creation(wd)
        self.return_to_group(wd)
        self.logout(wd)

    # Test Check for empty groups-------------------------------------
    def test_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username = "admin", password = "secret")
        self.open_groups(wd)
        self.init_group_creation(wd)
        self.fill_group_form(wd, Group(name = "", header = "", footer = ""))
        self.submit_group_creation(wd)
        self.return_to_group(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

