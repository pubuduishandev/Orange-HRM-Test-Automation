from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Step 1: Initialize WebDriver wait object for UI synchronization
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username, password):
        # Step 2: Locate the username field and input value
        username_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))

        # Step 3: Locate password field and login button
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        # Step 4: Clear and enter username
        username_input.clear()
        username_input.send_keys(username)

        # Step 5: Clear and enter password
        password_input.clear()
        password_input.send_keys(password)

        # Step 6: Click the login button to submit the form
        login_button.click()

    def is_dashboard_displayed(self):
        try:
            # Step 7: Wait for the Dashboard heading to appear
            dashboard_header = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
            )
            return dashboard_header.is_displayed()
        except:
            return False

    def get_login_error_message(self):
        try:
            # Step 8: Capture and return login error message (if any)
            error_locator = (By.XPATH, "//p[contains(text(), 'Invalid credentials')]")
            error_element = self.wait.until(EC.visibility_of_element_located(error_locator))
            return error_element.text
        except:
            return None
