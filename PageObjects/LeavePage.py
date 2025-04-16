from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_nav_item(self, nav_name):
        nav_xpath = f"//span[text()='{nav_name}']/ancestor::a"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, nav_xpath))).click()

    def get_page_header_text(self):
        header_xpath = "//h6"
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, header_xpath))).text