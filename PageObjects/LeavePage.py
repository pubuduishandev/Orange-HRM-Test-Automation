from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        # Step 1: Set up an explicit wait for reliable UI interaction
        self.wait = WebDriverWait(driver, 10)

    def click_quick_launch_button(self, button_title):
        """
        Clicks the Quick Launch button with the matching title.
        """
        # Step 2: Build XPath using the title and click the button
        button_locator = (By.XPATH, f"//button[@title='{button_title}']")
        self.wait.until(EC.element_to_be_clickable(button_locator)).click()

    def get_page_header_text(self):
        """
        Returns the header text of the currently navigated page.
        Assumes the header is within an <h6> element.
        """
        # Step 3: Locate the page header and return its trimmed text
        header_locator = (By.TAG_NAME, "h6")
        return self.wait.until(EC.presence_of_element_located(header_locator)).text.strip()

    def is_navigated_to_leave_page(self):
        """
        Returns True if the page header is 'Leave'.
        """
        # Step 4: Compare actual page header text with 'Leave'
        return self.get_page_header_text() == "Leave"
