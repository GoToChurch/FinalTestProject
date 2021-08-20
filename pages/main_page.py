from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By



class MainPage(BasePage): 
    def go_to_login_page(self):
        link = self.browser.find_element_by_css_selector("#login_link")
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Registration link is not presented"