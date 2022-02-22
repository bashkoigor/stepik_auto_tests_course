import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru", help="Choose language")


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    yield language


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

