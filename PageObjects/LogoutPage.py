from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.user_dropdown_toggle = (By.CLASS_NAME, "oxd-userdropdown-name")
        self.logout_link = (By.XPATH, "//a[text()='Logout']")

    def logout(self):
        # Click the dropdown to reveal the menu
        self.wait.until(EC.element_to_be_clickable(self.user_dropdown_toggle)).click()
        # Click the "Logout" link
        self.wait.until(EC.element_to_be_clickable(self.logout_link)).click()

    def is_logged_out(self):
        # Wait until the login page is visible (we’ll check for the username input field)
        login_input = (By.NAME, "username")
        return self.wait.until(EC.visibility_of_element_located(login_input)).is_displayed()
