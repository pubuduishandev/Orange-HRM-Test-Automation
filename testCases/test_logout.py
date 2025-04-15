import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.LogoutPage import LogoutPage
from PageObjects.HomePage import HomePage

@pytest.mark.order(4)
def test_logout_functionality(driver):
    home_page = HomePage(driver)
    home_page.load()

    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    assert login_page.is_dashboard_displayed()

    logout_page = LogoutPage(driver)
    logout_page.logout()
    assert logout_page.is_logged_out()
