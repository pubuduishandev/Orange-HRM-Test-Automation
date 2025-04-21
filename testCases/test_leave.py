import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.LeavePage import LeavePage
from Utilities.data_loader import load_quick_launch_items_from_json

# Step 1: Load test data from the JSON file containing Quick Launch items
test_data = load_quick_launch_items_from_json()

@pytest.mark.order(3)
@pytest.mark.parametrize("nav_item", test_data)
def test_navigate_to_leave(driver, nav_item):
    # Step 2: Initialize Page Objects for Home, Login, and Leave pages
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    leave_page = LeavePage(driver)

    # Step 3: Launch the homepage using URL from config
    home_page.load()

    # Step 4: Log in with valid credentials (static for now)
    login_page.login("Admin", "admin123")

    # Step 5: Assert dashboard is displayed post-login
    assert login_page.is_dashboard_displayed(), "Dashboard not displayed after login"

    # Step 6: Extract the 'button_title' from the current test dataset
    nav_name = nav_item["button_title"]

    # Step 7: Click the Quick Launch button that matches the title
    leave_page.click_quick_launch_button(nav_name)

    # Step 8: Retrieve the header text of the navigated page
    actual_header = leave_page.get_page_header_text()

    # Step 9: Validate that the navigation resulted in the 'Leave' page
    assert actual_header == "Leave", (
        f"\n[❌] Navigation failed for button: '{nav_name}'"
        f"\nExpected header: 'Leave'"
        f"\nActual header: '{actual_header}'"
    )
