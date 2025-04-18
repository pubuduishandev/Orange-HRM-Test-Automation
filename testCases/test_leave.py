import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.LeavePage import LeavePage
from Utilities.data_loader import load_side_nav_menu_items_from_json

# Step 1: Load navigation items from JSON (only nav_bar names)
test_data = load_side_nav_menu_items_from_json()

@pytest.mark.order(3)
@pytest.mark.parametrize("nav_item", test_data)
def test_navigate_to_leave(driver, nav_item):
    # Step 2: Load the homepage
    home_page = HomePage(driver)
    home_page.load()

    # Step 3: Perform login using valid credentials
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Step 4: Assert dashboard is displayed post-login
    assert login_page.is_dashboard_displayed(), "Dashboard not displayed after login"

    # Step 5: Initialize LeavePage for navigation
    leave_page = LeavePage(driver)

    # Step 6: Click the navigation item specified in test data
    nav_name = nav_item["nav_bar_item"]
    leave_page.click_nav_item(nav_name)

    # Step 7: Grab the current page's header text
    actual_header = leave_page.get_page_header_text()

    # Step 8: Define the expected header (only test passes if we land on "Leave")
    expected_header = "Leave"

    # Step 9: Assert the actual header matches "Leave"
    assert actual_header == expected_header, (
        f"\n[❌] Navigation failed for: '{nav_name}'"
        f"\nExpected to land on page with header: '{expected_header}'"
        f"\nBut actually landed on: '{actual_header}'"
    )
