from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_sale():
    browser = webdriver.Chrome()
    browser.get('https://magento.softwaretestingboard.com/')
    browser.implicitly_wait(5)
    sale_link = browser.find_element(By.ID, 'ui-id-8')
    sale_link.click()
    title = browser.find_element(By.TAG_NAME, 'h1')
    assert title.text == 'Sale'
