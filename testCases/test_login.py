import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from Utilities.data_loader import load_users_from_json

# Load test user data from JSON
test_users = load_users_from_json()

@pytest.mark.order(2)
@pytest.mark.parametrize("user", test_users)
def test_login_success(driver, user):
    # Step 1: Load the home page (login page)
    home_page = HomePage(driver)
    home_page.load()

    # Step 2: Perform login with provided user credentials
    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])

    # Step 3: Check if user is on the dashboard
    is_logged_in = login_page.is_dashboard_displayed()

    # Step 4: Get error message if login failed
    error_msg = login_page.get_login_error_message()

    # Step 5: Expected behavior
    expected_success = user["username"] == "Admin" and user["password"] == "admin123"

    # Step 6: Assert based on expected outcome
    if expected_success:
        assert is_logged_in, f"Login successful with'{user['username']} & {user['password']}'!"
    else:
        assert error_msg == "Invalid credentials", (
            f"'{user['username']} & {user['password']}' are Invalid credentials!"
        )
