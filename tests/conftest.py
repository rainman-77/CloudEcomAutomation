import logging
import os
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from utilities import read_configurations as rc


global driver


# Logging setup for parallel execution
def pytest_configure(config):
    # Get the worker ID from the pytest-xdist environment
    worker_id = os.environ.get('PYTEST_XDIST_WORKER', 'master')  # 'master' for single-threaded mode
    log_file = f"logs/automation_worker_{worker_id}.log"

    # Configure logging
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s: %(levelname)s: %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )
    logging.info("....starting test setup....\n")


@pytest.fixture()
def log_on_failure(request):
    global driver
    yield
    item = request.node     # for allure reporting
    if item.rep_call.failed:    # takes screenshots only for failed test case & attaches to allure
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)   # for allure reporting
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def setup_and_teardown(request, worker_id):
    global driver
    browser = None
    options = None
    exec_mode = rc.read_configuration("basic info", "execution")
    run_env = rc.read_configuration("basic info", "run_environment")
    browser_mode = rc.read_configuration("basic info", "browser_mode")

    if exec_mode == 'standalone':
        browser = rc.read_configuration("basic info", "browser")  # uses config.ini to get specific browser instance
        logging.info(f"Running test in '{browser_mode}-{exec_mode}' mode on '{browser}' browser in '{run_env}' environment")

    elif exec_mode == 'parallel':
        # worker specific browser will be selected like gw0-chrome,gw1-firefox,gw2-edge for even parallel execution
        browsers = ["chrome", "firefox", "edge"]
        browser = browsers[int(worker_id.lstrip("gw")) % len(browsers)]
        logging.info(f"Running test in '{browser_mode}-{exec_mode}' mode on '{browser}' in '{run_env}' environment")

    if browser == 'chrome':
        options = ChromeOptions()
        if browser_mode == 'headless':  # now added headless test here
            options.add_argument("--headless")
        if run_env == 'local':
            driver = webdriver.Chrome(options=options)

    elif browser == 'firefox':
        options = FirefoxOptions()
        if browser_mode == 'headless':
            options.add_argument("--headless")
        if run_env == 'local':
            driver = webdriver.Firefox(options=options)

    elif browser == 'edge':
        options = EdgeOptions()
        if browser_mode == 'headless':
            options.add_argument("--headless")
        if run_env == 'local':
            driver = webdriver.Edge(options=options)

    else:
        raise ValueError("provide valid browser name in config.ini file")

    if run_env == 'remote':
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',  # for selenium grid's hub
            # command_executor='http://localhost:4444',   # for selenium standalone grid
            options=options
        )

    driver.maximize_window()
    url = rc.read_configuration("basic info", "url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()
