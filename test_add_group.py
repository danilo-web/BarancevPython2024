# -*- coding: utf-8 -*-
from selenium import webdriver
from group import Group
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def test_add_group(self):
        self.login(Username="admin", Password="secret")
        self.new_group_creation(Group(name="test", header="tetete", footer="hjmjhgfd"))
        self.logout()

    def test_add_empty_group(self):
        self.login(Username="admin", Password="secret")
        self.new_group_creation(Group(name="", header="", footer=""))
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def new_group_creation(self, group):
        wd = self.wd
        #open_group_page
        wd.find_element_by_link_text("groups").click()
        # new_group_creation
        wd.find_element_by_name("new").click()
        # fill_group_data
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit_group_creation
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()

    def login(self, Username, Password):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(Username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(Password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

