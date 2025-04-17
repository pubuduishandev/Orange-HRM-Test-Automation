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

    # Step 3: Verify if dashboard is displayed after login
    is_logged_in = login_page.is_dashboard_displayed()

    # Step 4: Define expected result — Only allow success for the known valid credentials
    expected = user["username"] == "Admin" and user["password"] == "admin123"

    # Step 5: Assert actual vs expected login result
    assert is_logged_in == expected, (
        f"Login test failed for user: {user['username']} | "
        f"Expected login success: {expected}, Actual: {is_logged_in}"
    )