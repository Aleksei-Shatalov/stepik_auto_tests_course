from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "In basket items is presented, but should not be"
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), \
            "Basket empty message is not presented, but should be"
