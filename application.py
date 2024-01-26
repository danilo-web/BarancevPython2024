from selenium import WebDriver
#from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver.Firefox()
        self.wd.implicitly_wait(30)

        