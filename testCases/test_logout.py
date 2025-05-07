import pytest
import os
from datetime import datetime
from PageObjects.LoginPage import LoginPage
from PageObjects.LogoutPage import LogoutPage
from PageObjects.HomePage import HomePage
from Utilities.data_loader import load_profile_menu_items_from_json

# Step 1: Proactively create the Screenshots folder if it doesn't exist
screenshot_dir = os.path.join("Screenshots", "Test Logout")
os.makedirs(screenshot_dir, exist_ok=True)

# Step 2: Load base URLs from test data JSON
test_data = load_profile_menu_items_from_json()

@pytest.mark.order(4)
@pytest.mark.parametrize("menu_item", test_data)
def test_logout_functionality(driver, menu_item):
    # Step 3: Load the app and login
    home_page = HomePage(driver)
    home_page.load()

    # Step 4: Log in with valid credentials (static for now)
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Step 5: Assert login was successful by checking dashboard visibility
    assert login_page.is_dashboard_displayed(), "Login failed — Dashboard not visible"

    # Step 6: Extract the dropdown item from test data
    dropdown_item = menu_item["drop_down"]

    # Step 7: Click the dropdown item using LogoutPage's generic method
    logout_page = LogoutPage(driver)
    logout_page.click_dropdown_option(dropdown_item)

    # Step 8: Check if clicking that item led to the login page (i.e., user got logged out)
    try:
        assert logout_page.is_logged_out(), (
            f"[❌] Clicked '{dropdown_item}' but did NOT redirect to login page. "
            "Expected logout behavior not observed."
        )
        print(f"[✅] Clicked '{dropdown_item}' → successfully logged out.")
    except AssertionError as e:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(screenshot_dir, f"logout_failure_{dropdown_item}_{timestamp}.png")
        driver.save_screenshot(filename)
        print(f"[📸] Screenshot captured on logout failure: {filename}")
        raise e
