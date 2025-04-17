from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_nav_item(self, nav_name):
        """
        Clicks a side navigation item based on the provided visible text.
        Example: nav_name = "Leave" will click the 'Leave' menu item.
        """
        # Step 1: Construct the XPath to locate the sidebar nav item by its visible text
        nav_xpath = f"//span[text()='{nav_name}']/ancestor::a"

        # Step 2: Wait for the nav item to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.XPATH, nav_xpath))).click()

    def get_page_header_text(self):
        """
        Retrieves the visible page header text after navigation.
        Used to confirm the page loaded correctly.
        """
        # Step 3: Wait until the page header <h6> element is visible and extract its text
        header_xpath = "//h6"
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, header_xpath))).text