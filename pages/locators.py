from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
    
class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-succes")