import pytest
from selenium.webdriver.common.by import By
import time
import math

link_list = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.mark.parametrize('link', link_list)
class TestLogin:
    def test_guest_should_see_login_link(self, browser, link):
        answer = math.log(int(time.time()))
        browser.get(link)
        time.sleep(5)
        textarea = browser.find_element(By.TAG_NAME, "textarea")
        textarea.send_keys(answer)
        time.sleep(2)
        button = browser.find_element(By.CLASS_NAME, "submit-submission")
        button.click()
        time.sleep(10)
        feedback = browser.find_element(By.TAG_NAME, "pre")
        feedback = feedback.text
        assert feedback == "Correct!", "Text does not match!"

