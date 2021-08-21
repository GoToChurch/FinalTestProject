from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage): 
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
           "Basket is not empty, but should be"
    
    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
           "There is no empty basket message, but should be"
    