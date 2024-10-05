import pytest
from selenium import webdriver
from utilities import read_configurations as rc


global driver


@pytest.fixture()
def log_on_failure(request):
    global driver
    yield


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    driver = webdriver.Chrome()

    driver.maximize_window()
    url = rc.read_configuration("basic info", "url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()
