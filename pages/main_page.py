from .base_page import BasePage
from selenium.webdriver.common.by import By
import time
from .login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

