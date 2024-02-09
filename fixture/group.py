from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app
        self.group_cache = None

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # new_group_creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit_group_creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def modify_first_group(self):
        self.modify_group_by_index(index=0)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        # select any group and edit
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_xpath("(//input[@name='edit'])").click()
        # fill_group_data
        self.fill_group_form(new_group_data)
        # submit_modification
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def open_group_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/group.php"):  # len(wd.find_elements_by_name("new")) > 0: - это условие сильно
            # тормозит процесс, а при использовании обоих вообще не работает
            wd.find_element_by_link_text("groups").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                element_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, element_id=element_id))
        return list(self.group_cache)
