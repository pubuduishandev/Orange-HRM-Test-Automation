import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.LeavePage import LeavePage
from Utilities.data_loader import load_side_nav_menu_from_json

test_data = load_side_nav_menu_from_json()

@pytest.mark.order(3)
@pytest.mark.parametrize("nav_item", test_data)
def test_navigate_to_leave(driver, nav_item):
    # Step 1: Login
    home_page = HomePage(driver)
    home_page.load()

    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    assert login_page.is_dashboard_displayed(), "Dashboard not displayed after login"

    # Step 2: Click side nav item
    leave = LeavePage(driver)
    leave.click_nav_item(nav_item["nav_bar"])

    # Step 3: Capture actual page header from UI
    actual_header = leave.get_page_header_text()

    # Step 4: Strict assertion - both values must be 'Leave'
    expected_nav = "Leave"
    expected_header = "Leave"

    assert nav_item["nav_bar"] == expected_nav, f"Expected nav_bar='{expected_nav}', got '{nav_item['nav_bar']}'"
    assert nav_item["page_header"] == expected_header, f"Expected page_header='{expected_header}', got '{nav_item['page_header']}'"
    assert actual_header == expected_header, f"Expected header '{expected_header}', got '{actual_header}' after clicking '{nav_item['nav_bar']}'"