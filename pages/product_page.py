from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage): 
    def add_item_to_basket(self):
        link = self.browser.find_element_by_css_selector(".btn-add-to-basket")
        link.click()
        
    def should_be_equal_price(self):
        item_price = self.browser.find_element_by_css_selector("p.price_color")
        price = item_price.text
        alert_price = self.browser.find_elements_by_xpath(f"//strong[text()='{price}']")
        assert len(alert_price) > 0, "Prices didn't match"
    
    def should_be_same_name(self):
        item_name = self.browser.find_element_by_css_selector(".product_main>h1")
        name = item_name.text
        alert_name = self.browser.find_elements_by_xpath(f'//strong[(text()="{name}")]')
        assert len(alert_name) > 0, "Item names didn't match"
    
    def show_current_url(self):
        url = self.browser.current_url
        print(url)
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
    
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is not disappeared"