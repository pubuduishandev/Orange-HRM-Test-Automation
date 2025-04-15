import pytest
from selenium import webdriver
from datetime import datetime
from Utilities.log_report import initialize_log, record_test_start, record_test_end

test_cases_map = {
    "test_home_page_title": ("TC01", "Show Home Page Title"),
    "test_login_success": ("TC02", "Login Functionality"),
    "test_navigate_to_leave": ("TC03", "Leave Functionality"),
    "test_logout_functionality": ("TC04", "Logout Functionality"),
}

test_start_times = {}
test_end_times = {}

# WebDriver setup
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# Initialize log file once
def pytest_sessionstart(session):
    initialize_log()

# Track first start time of a base test function
def pytest_runtest_setup(item):
    base_name = item.originalname  # base test name without param
    if base_name not in test_start_times:
        test_start_times[base_name] = record_test_start()

# Track latest end time per base test
def pytest_runtest_teardown(item, nextitem):
    base_name = item.originalname
    test_end_times[base_name] = datetime.now()

# Write final log only once per test case after all tests run
def pytest_sessionfinish(session, exitstatus):
    for base_name, start_time in test_start_times.items():
        end_time = test_end_times.get(base_name)
        if end_time:
            test_id, desc = test_cases_map.get(base_name, ("TCXX", "Unknown Test"))
            record_test_end(test_id, desc, start_time, end_time)
