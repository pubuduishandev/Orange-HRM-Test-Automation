from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Locators for login page elements
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")

    def login(self, username, password):
        """
        Performs the login action using provided credentials.
        """
        # Step 1: Enter username
        self.wait.until(EC.presence_of_element_located(self.username_input)).send_keys(username)

        # Step 2: Enter password
        self.wait.until(EC.presence_of_element_located(self.password_input)).send_keys(password)

        # Step 3: Click the login button
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def is_dashboard_displayed(self):
        """
        Verifies if the dashboard is displayed after login.
        """
        # Step 4: Wait for dashboard header to become visible as a login success indicator
        return self.wait.until(EC.visibility_of_element_located(self.dashboard_header)).is_displayed()