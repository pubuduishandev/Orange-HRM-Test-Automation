import pytest
import os
from datetime import datetime
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from Utilities.data_loader import load_users_from_json

# Step 1: Create Screenshots folder if it doesn't exist
screenshot_dir = os.path.join("Screenshots", "Test Login")
os.makedirs(screenshot_dir, exist_ok=True)

# Step 2: Load test users from JSON
test_data = load_users_from_json()

@pytest.mark.order(2)
@pytest.mark.parametrize("credential", test_data)
def test_login_success(driver, credential):
    # Step 3: Load login page
    home_page = HomePage(driver)
    home_page.load()

    # Step 4: Attempt login with provided credentials
    login_page = LoginPage(driver)
    login_page.login(credential["username"], credential["password"])

    # Step 5: Check if Dashboard is displayed
    if login_page.is_dashboard_displayed():
        print(f"[✅] Login passed with: {credential['username']} / {credential['password']}")
        assert True
    else:
        # Step 6: Take screenshot on failure
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(
            screenshot_dir,
            f"login_failure_{credential['username']}-{credential['password']}_{timestamp}.png"
        )
        driver.save_screenshot(filename)

        # Step 7: Grab error message if present
        error_msg = login_page.get_login_error_message()

        print(f"\n[❌] Login failed for {credential['username']} / {credential['password']}")
        print(f"[📸] Screenshot saved to: {filename}")
        if error_msg:
            print(f"[⚠️] Error Message Displayed: {error_msg}")
        assert False, f"Login failed. Invalid Credentials: {credential['username']} & {credential['password']}"
