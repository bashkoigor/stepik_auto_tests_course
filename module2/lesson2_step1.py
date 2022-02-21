from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
   
    result = int(num1.text) + int(num2.text)
    
    print(num1.text)
    print(num2.text)
    print(result)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(result))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(3)
    browser.quit()

