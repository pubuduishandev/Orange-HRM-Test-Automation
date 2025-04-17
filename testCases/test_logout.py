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

    # Step 2: Check if the current test menu item is 'Logout'
    expected_dropdown_item = "Logout"
    actual_item = menu_item["drop_down"]

    if actual_item != expected_dropdown_item:
        pytest.fail(f"Test failed — Expected dropdown item 'Logout' but got '{actual_item}'")
    else:
        # Step 3: Attempt logout
        logout_page = LogoutPage(driver)
        logout_page.logout()

        # Step 4: Verify logout was successful
        if logout_page.is_logged_out():
            print("Logout test case pass")
        else:
            pytest.fail("Logout failed — login page not visible after logout")
