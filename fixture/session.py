import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        # time.sleep(0.1)  # без этого при запуске всех тестов сразу logout не выполняется и тесты виснут

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//b[text()='(admin)']").text[1:-1]

    def ensure_logout(self):
        wd = self.app.wd
        if len(wd.find_elements_by_link_text("Logout")) > 0:
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if len(wd.find_elements_by_link_text("Logout")) > 0:
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
