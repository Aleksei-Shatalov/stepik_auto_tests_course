import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://google.com'
try:
    # open google.com
    browser.get(url)
    search = browser.find_element(By.TAG_NAME, "textarea")
    # search request test
    search.send_keys('test')
    search.send_keys(Keys.RETURN)

    link = browser.find_element(By.LINK_TEXT, "TEST Definition & Meaning")
    link.click()

    time.sleep(5)

finally:
    browser.quit()