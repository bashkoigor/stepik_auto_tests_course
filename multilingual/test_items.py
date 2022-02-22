from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_multilingual(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get(link)
    button_present = True
    try:
        browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form button.btn")
    except NoSuchElementException:
        button_present = False

    assert button_present, "Button dose not exist!"

