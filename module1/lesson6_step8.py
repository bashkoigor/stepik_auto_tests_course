from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_block .first_class input ")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block .second_class input ")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".first_block .third_class input ")
    input3.send_keys("Smolensk@mail.ru")
    input4 = browser.find_element_by_css_selector(".second_block .first_class input")
    input4.send_keys("1234567")
    input5 = browser.find_element_by_css_selector(".second_block .second_class input")
    input5.send_keys("Russia")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
    


