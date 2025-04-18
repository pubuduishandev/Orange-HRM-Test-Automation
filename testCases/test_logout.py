import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.LogoutPage import LogoutPage
from PageObjects.HomePage import HomePage
from Utilities.data_loader import load_profile_menu_items_from_json

# Step 1: Load dropdown items from JSON (to be clicked from profile dropdown)
test_data = load_profile_menu_items_from_json()

@pytest.mark.order(4)
@pytest.mark.parametrize("menu_item", test_data)
def test_logout_functionality(driver, menu_item):
    # Step 2: Load the app and login
    home_page = HomePage(driver)
    home_page.load()

    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Step 3: Assert login was successful by checking dashboard visibility
    assert login_page.is_dashboard_displayed(), "Login failed — Dashboard not visible"

    # Step 4: Extract the dropdown item from test data
    dropdown_item = menu_item["drop_down"]

    # Step 5: Click the dropdown item using LogoutPage's generic method
    logout_page = LogoutPage(driver)
    logout_page.click_dropdown_option(dropdown_item)

    # Step 6: Check if clicking that item led to the login page (i.e., user got logged out)
    if logout_page.is_logged_out():
        print(f"[✅] Clicked '{dropdown_item}' → successfully logged out.")
    else:
        pytest.fail(
            f"[❌] Clicked '{dropdown_item}' but did NOT redirect to login page. "
            "Expected logout behavior not observed."
        )
