from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session2 import SessionHelper
from newcontact import ContactHelper

class Application_contact:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def destroy_page(self):
        self.wd.quit()