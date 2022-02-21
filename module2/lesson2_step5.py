from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)

    element = browser.find_element_by_id("input_value")
    y = calc(element.text)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

