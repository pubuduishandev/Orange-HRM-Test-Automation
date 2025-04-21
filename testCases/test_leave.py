import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.LeavePage import LeavePage
from Utilities.data_loader import load_quick_launch_items_from_json

# Step 1: Load quick launch test data from JSON
test_data = load_quick_launch_items_from_json()

@pytest.mark.order(3)
@pytest.mark.parametrize("button", test_data)
def test_navigate_to_leave(driver, button):
    # Step 2: Initialize HomePage and launch the application
    home_page = HomePage(driver)
    home_page.load()

    # Step 3: Perform login using valid credentials
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Step 4: Assert that the dashboard appears, indicating a successful login
    assert login_page.is_dashboard_displayed(), "Dashboard not displayed after login"

    # Step 5: Initialize the LeavePage object
    leave_page = LeavePage(driver)

    # Step 6: Extract the button title to be clicked from the test data
    button_name = button["button_title"]

    # Step 7: Click the correct quick launch button based on the title
    leave_page.click_nav_item(button_name)

    # Step 8: Get the page header after navigation
    actual_header = leave_page.get_page_header_text()

    # Step 9: Assert that we have landed on the correct page (Leave)
    assert actual_header == "Leave", (
        f"\n[❌] Navigation failed for: '{button_name}'"
        f"\nExpected to land on page with header: 'Leave'"
        f"\nBut actually landed on: '{actual_header}'"
    )
