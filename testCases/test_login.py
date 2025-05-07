import pytest
import os
from datetime import datetime
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from Utilities.data_loader import load_users_from_json

# Step 1: Proactively create the Screenshots folder if it doesn't exist
screenshot_dir = os.path.join("Screenshots", "Test Login")
os.makedirs(screenshot_dir, exist_ok=True)

# Step 2: Load base URLs from test data JSON
test_users = load_users_from_json()

@pytest.mark.order(2)
@pytest.mark.parametrize("user", test_users)
def test_login_success(driver, user):
    # Step 2: Load the home page (login page)
    home_page = HomePage(driver)
    home_page.load()

    # Step 3: Perform login with provided user credentials
    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])

    # Step 4: Check if user is on the dashboard
    is_logged_in = login_page.is_dashboard_displayed()

    # Step 5: Get error message if login failed
    error_msg = login_page.get_login_error_message()

    # Step 6: Expected behavior
    expected_success = user["username"] == "Admin" and user["password"] == "admin123"

    # Step 7: Assert based on expected outcome
    try:
        if expected_success:
            assert is_logged_in, f"Login failed with correct credentials: '{user['username']}'"
        else:
            assert error_msg == "Invalid credentials", (
                f"Expected 'Invalid credentials' but got: {error_msg}"
            )
    except AssertionError as e:
        # Step 8: Capture screenshot on failure
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(
            screenshot_dir,
            f"login_{user['username']}_{timestamp}_screenshot.png"
        )
        driver.save_screenshot(filename)
        print(f"\n[📸] Screenshot saved to: {filename}")
        raise e
