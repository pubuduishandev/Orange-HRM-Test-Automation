import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.LeavePage import LeavePage

@pytest.mark.usefixtures("driver")
class TestLeaveFunctionality:

    @pytest.mark.order(3)
    def test_navigate_to_leave(self, driver):
        home_page = HomePage(driver)
        home_page.load()

        login_page = LoginPage(driver)
        login_page.login("Admin", "admin123")

        assert login_page.is_dashboard_displayed()

        leave = LeavePage(driver)
        leave.click_leave_menu()
        assert leave.is_leave_page_displayed()
