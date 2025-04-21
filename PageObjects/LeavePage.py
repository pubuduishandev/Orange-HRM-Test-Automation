from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_quick_launch_button(self, button_title):
        """
        Clicks the Quick Launch button with the matching title.
        """
        button_locator = (By.XPATH, f"//button[@title='{button_title}']")
        self.wait.until(EC.element_to_be_clickable(button_locator)).click()

    def get_page_header_text(self):
        """
        Returns the header text of the currently navigated page.
        Assumes the header is within an <h6> element.
        """
        header_locator = (By.TAG_NAME, "h6")
        return self.wait.until(EC.presence_of_element_located(header_locator)).text.strip()

    def is_navigated_to_leave_page(self):
        """
        Returns True if the page header is 'Leave'.
        """
        return self.get_page_header_text() == "Leave"
