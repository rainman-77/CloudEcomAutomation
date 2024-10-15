import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from utilities import read_configurations as rc


global driver


@pytest.fixture()
def log_on_failure(request):
    global driver
    yield


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = rc.read_configuration("basic info", "browser")

    if browser == 'chrome':
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif browser == 'edge':
        options = EdgeOptions()
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError("provide valid browser name in config.ini file")

    driver.maximize_window()
    url = rc.read_configuration("basic info", "url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()
