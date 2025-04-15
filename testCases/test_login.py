import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from Utilities.data_loader import load_users_from_json

test_users = load_users_from_json()

@pytest.mark.order(2)
@pytest.mark.parametrize("user", test_users)
def test_login_success(driver, user):
    home_page = HomePage(driver)
    home_page.load()

    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])

    is_logged_in = login_page.is_dashboard_displayed()
    expected = user["username"] == "Admin" and user["password"] == "admin123"

    assert is_logged_in == expected