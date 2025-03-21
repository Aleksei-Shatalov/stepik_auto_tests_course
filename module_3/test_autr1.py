import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import os
from dotenv import load_dotenv

load_dotenv()
STEPIK_EMAIL = os.getenv('STEPIK_EMAIL')
STEPIK_PASSWORD = os.getenv('STEPIK_PASSWORD')



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()


link = "https://stepik.org/lesson/236905/step/1"

def test_autorization(browser):
    browser.get(link)

    # авторизация
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "ember466"))
    )
    button.click()
    input1 = browser.find_element(By.ID, "id_login_email")
    input1.send_keys(STEPIK_EMAIL)
    input2 = browser.find_element(By.ID, "id_login_password")
    input2.send_keys(STEPIK_PASSWORD)
    button1 = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
    button1.click()

    # кнопка решить заново
    try:
        time.sleep(10)
        button2 = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn"))
        )
        #button2 = browser.find_element(By.CSS_SELECTOR, "button.again-btn")
        button2.click()
        button3 = browser.find_element(By.XPATH, '//button[text()="OK"]')
        button3.click()

        # ввод ответа
        input3 = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.ember-text-area"))
        )
        # input3 = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
        answer = math.log(int(time.time()))
        input3.send_keys(answer)
        button4 = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        # button4 = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        button4.click()
    except:
        # ввод ответа
        input3 = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.ember-text-area"))
        )
        #input3 = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
        answer = math.log(int(time.time()))
        input3.send_keys(answer)
        button4 = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        #button4 = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        button4.click()

    finally:
        # проверка сообщения
        feedback_text_elt = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p.smart-hints__hint"))
        )
        #feedback_text_elt = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
        f_text = feedback_text_elt.text
        print(f_text)
        assert f_text == "Correct!"
        time.sleep(1)

if __name__ == "__main__":
    pytest.main()
