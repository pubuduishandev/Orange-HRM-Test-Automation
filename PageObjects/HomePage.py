from Utilities.read_config import read_config

class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Step 1: Read the base URL from the config file at initialization
        self.url = read_config("DEFAULT", "base_url")  # Dynamically fetched from config

    def load(self):
        """
        Loads the home page using the URL fetched from config.
        """
        # Step 2: Navigate the browser to the homepage URL
        self.driver.get(self.url)

    def get_title(self):
        """
        Returns the title of the current page.
        Used to validate that the homepage has loaded correctly.
        """
        # Step 3: Return the page title
        return self.driver.title
