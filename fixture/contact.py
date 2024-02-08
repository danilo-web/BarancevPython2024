import time
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.group_cache = None

    def create(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.open_contact_page()
        self.group_cache = None

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        self.select_first_contact()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.open_contact_page()
        self.group_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_contact_page()
        self.group_cache = None

    def open_contact_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0:
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@src='icons/pencil.png'])").click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        time.sleep(1)

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_xpath("(//img[@src='icons/pencil.png'])"))

    def get_contact_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.group_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                element_id = element.find_element_by_xpath(".//td[1]//input").get_attribute("value")
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                self.group_cache.append(Contact(firstname=firstname, lastname=lastname, element_id=element_id))
        return list(self.group_cache)
