import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.LogoutPage import LogoutPage
from PageObjects.HomePage import HomePage
from Utilities.data_loader import load_profile_menu_from_json

# Load profile dropdown test data
profile_items = load_profile_menu_from_json()

@pytest.mark.order(4)
@pytest.mark.parametrize("menu_item", profile_items)
def test_logout_functionality(driver, menu_item):
    # Step 1: Launch app and log in
    home_page = HomePage(driver)
    home_page.load()

    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    assert login_page.is_dashboard_displayed(), "Login failed — dashboard not visible"

    # Step 2: Attempt logout ONLY if the dropdown item is "Logout"
    logout_page = LogoutPage(driver)

    expected_dropdown_item = "Logout"

    # Step 3: Strictly validate dropdown label before attempting
    assert menu_item["drop_down"] == expected_dropdown_item, (
        f"Test failed — Expected dropdown item 'Logout' but got '{menu_item['drop_down']}'"
    )

    # Step 4: Proceed to logout (click and verify logout works)
    logout_page.logout()
    assert logout_page.is_logged_out(), "Logout failed — login page not visible after logout"
