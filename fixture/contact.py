import time
import re
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.contact_cache = None

    def create(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.open_contact_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.open_contact_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_contact_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("(//img[@src='icons/pencil.png'])")[index].click()

    def open_contact_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/"):
            wd.find_element_by_link_text("home").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        time.sleep(1)

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_xpath("(//img[@src='icons/pencil.png'])"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                element_id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(element_id=element_id, firstname=firstname, lastname=lastname,
                                                  address=address, all_emails_from_homepage=all_emails,
                                                  all_phones_from_homepage=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        element_id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(element_id=element_id, firstname=firstname, lastname=lastname, address=address,
                       email=email, email2=email2, email3=email3, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone)

