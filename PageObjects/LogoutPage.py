from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

        # Step 1: Create an explicit wait object
        self.wait = WebDriverWait(self.driver, 10)

        # Step 2: Define locator for user dropdown toggle (profile picture)
        self.user_dropdown_toggle = (By.CLASS_NAME, "oxd-userdropdown-name")

    def click_dropdown_option(self, option_text):
        """
        Clicks the user dropdown and selects an item by visible text (e.g., 'Logout', 'Support').
        """
        # Step 3: Click the profile icon to expand the dropdown menu
        self.wait.until(EC.element_to_be_clickable(self.user_dropdown_toggle)).click()

        # Step 4: Build the XPath dynamically using dropdown text
        dropdown_option = (By.XPATH, f"//a[normalize-space()='{option_text}']")

        # Step 5: Click the specified dropdown option (like Logout, Profile, etc.)
        self.wait.until(EC.element_to_be_clickable(dropdown_option)).click()

    def logout(self):
        """
        Shortcut method to directly logout by selecting 'Logout' from dropdown.
        """
        # Step 6: Click Logout using the reusable method
        self.click_dropdown_option("Logout")

    def is_logged_out(self):
        """
        Verifies if the user is successfully logged out by checking for the presence
        of the <auth-login> tag, which only appears on the login page.
        """
        try:
            # Step 7: Confirm login page is displayed by detecting <auth-login> tag
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "auth-login")))
            return True
        except:
            return False
