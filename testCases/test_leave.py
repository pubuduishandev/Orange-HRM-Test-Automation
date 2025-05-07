import pytest
import os
from datetime import datetime
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.LeavePage import LeavePage
from Utilities.data_loader import load_quick_launch_items_from_json

# Step 1: Proactively create the Screenshots folder if it doesn't exist
screenshot_dir = os.path.join("Screenshots", "Test Leave")
os.makedirs(screenshot_dir, exist_ok=True)

# Step 2: Load base URLs from test data JSON
test_data = load_quick_launch_items_from_json()

@pytest.mark.order(3)
@pytest.mark.parametrize("nav_item", test_data)
def test_navigate_to_leave(driver, nav_item):
    # Step 3: Initialize Page Objects for Home, Login, and Leave pages
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    leave_page = LeavePage(driver)

    # Step 4: Launch the homepage using URL from config
    home_page.load()

    # Step 5: Log in with valid credentials (static for now)
    login_page.login("Admin", "admin123")

    # Step 6: Assert dashboard is displayed post-login
    assert login_page.is_dashboard_displayed(), "Dashboard not displayed after login"

    # Step 7: Extract the 'button_title' from the current test dataset
    nav_name = nav_item["button_title"]

    # Step 8: Click the Quick Launch button that matches the title
    leave_page.click_quick_launch_button(nav_name)

    # Step 9: Retrieve the header text of the navigated page
    actual_header = leave_page.get_page_header_text()

    # Step 10: Validate that the navigation resulted in the 'Leave' page
    try:
        assert actual_header == "Leave", "Navigation to Leave page failed"
    except AssertionError as e:
        # Step 11: Capture screenshot on failure
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(screenshot_dir, f"test_failure_{timestamp}_screenshot.png")
        driver.save_screenshot(filename)
        print(f"\n[📸] Screenshot saved to: {filename}")
        raise e  # Re-raise to let pytest handle the failure
