import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.LeavePage import LeavePage
from Utilities.data_loader import load_side_nav_menu_from_json

# Load test user data from JSON
test_data = load_side_nav_menu_from_json()

@pytest.mark.order(3)
@pytest.mark.parametrize("nav_item", test_data)
def test_navigate_to_leave(driver, nav_item):
    # Step 1: Login
    home_page = HomePage(driver)
    home_page.load()

    # Step 2: Perform login with provided user credentials
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    assert login_page.is_dashboard_displayed(), "Dashboard not displayed after login"

    # Step 3: Click side nav item
    leave = LeavePage(driver)
    leave.click_nav_item(nav_item["nav_bar"])

    # Step 4: Capture actual page header from UI
    actual_header = leave.get_page_header_text()

    # Step 5: Strict assertion - both values must be 'Leave'
    expected_nav = "Leave"
    expected_header = "Leave"

    # Step 6: Assert actual vs expected navigate to the leave result
    assert nav_item["nav_bar"] == expected_nav, f"Expected click on quick launch ='{expected_nav}', but clicked on '{nav_item['nav_bar']}'"
    assert nav_item["page_header"] == expected_header, f"Expected ='{expected_header}', got '{nav_item['page_header']}'"
    assert actual_header == expected_header, f"Expected header '{expected_header}', got '{actual_header}' after clicking '{nav_item['nav_bar']}'"