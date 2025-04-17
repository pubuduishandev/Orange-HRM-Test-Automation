from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Dropdown toggle element (click to open the dropdown)
        self.user_dropdown_toggle = (By.CLASS_NAME, "oxd-userdropdown-name")

    def click_dropdown_option(self, option_text):
        """
        Clicks the user dropdown and selects an item by visible text (e.g., 'Logout', 'Support').
        """
        # Step 1: Click the dropdown to reveal the menu
        self.wait.until(EC.element_to_be_clickable(self.user_dropdown_toggle)).click()

        # Step 2: Dynamically build the locator for the desired dropdown item
        dropdown_option = (By.XPATH, f"//a[normalize-space()='{option_text}']")

        # Step 3: Click the requested dropdown item
        self.wait.until(EC.element_to_be_clickable(dropdown_option)).click()

    def logout(self):
        """
        Shortcut method to directly logout by selecting 'Logout' from dropdown.
        """
        self.click_dropdown_option("Logout")

    def is_logged_out(self):
        """
        Verifies if the user is successfully logged out by checking for the presence
        of the <auth-login> tag, which only appears on the login page.
        """
        try:
            # Wait until the auth-login tag is visible (indicative of login page)
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "auth-login")))
            return True
        except:
            return False
