from selenium.webdriver.common.by import By



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONF_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6 h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6 p.price_color")
    BOOK_NAME_BASKET = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    BOOK_PRICE_BASKET = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")

class BasketPageLocators():
    BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")

