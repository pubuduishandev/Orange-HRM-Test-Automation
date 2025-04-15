from Utilities.read_config import read_config

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = read_config("DEFAULT", "base_url")  # Dynamically fetched from config

    def load(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title
