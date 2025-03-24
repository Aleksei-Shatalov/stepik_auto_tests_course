from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
import math



class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def check_book_name_price(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_name_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_BASKET)
        book_price_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_BASKET)
        assert book_name.text == book_name_basket.text, "Название книги не совпадает"
        assert book_price.text == book_price_basket.text, "Цена книги не совпадает"
        print(book_name_basket.text)
        print(book_price_basket.text)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"