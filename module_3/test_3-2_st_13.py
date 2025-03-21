from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "input.first:required")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.second:required")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.third:required")
        input3.send_keys("ivan@example.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(10)
        browser.quit()

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "input.first:required")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.second:required")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.third:required")
        input3.send_keys("ivan@example.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    unittest.main()

