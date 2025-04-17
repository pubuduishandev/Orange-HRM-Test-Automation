from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username, password):
        username_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        login_button.click()

    def is_dashboard_displayed(self):
        try:
            dashboard_header = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
            )
            return dashboard_header.is_displayed()
        except:
            return False

    def get_login_error_message(self):
        try:
            error_locator = (By.XPATH, "//p[contains(text(), 'Invalid credentials')]")
            error_element = self.wait.until(EC.visibility_of_element_located(error_locator))
            return error_element.text
        except:
            return None
