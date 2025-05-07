import pytest
import os
from datetime import datetime
from PageObjects.HomePage import HomePage
from Utilities.data_loader import load_urls_from_json

# Step 1: Proactively create the Screenshots folder if it doesn't exist
screenshot_dir = os.path.join("Screenshots", "Test Home")
os.makedirs(screenshot_dir, exist_ok=True)

# Step 2: Load base URLs from test data JSON
test_urls = load_urls_from_json()

@pytest.mark.order(1)
@pytest.mark.parametrize("url_data", test_urls)
def test_home_page_title(driver, url_data):
    # Step 3: Extract base URL from the current dataset
    base_url = url_data["base_url"]

    # Step 4: Initialize the HomePage object (uses WebDriver instance)
    home_page = HomePage(driver)

    # Step 5: Override the homepage URL with test data (bypasses config)
    home_page.url = base_url

    # Step 6: Navigate to the base URL
    home_page.load()

    # Step 7: Retrieve the current page title
    actual_title = home_page.get_title()

    # Step 8: Define the expected title string for OrangeHRM
    expected_title = "OrangeHRM"

    # Step 9: Compare the actual title with expected title using exact match
    try:
        assert actual_title.strip() == expected_title, (
            f"\n[❌] Title mismatch for: {base_url}"
            f"\nExpected: {expected_title}"
            f"\nActual: {actual_title}"
        )
    except AssertionError as e:
        # Step 10: Capture screenshot on failure
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(screenshot_dir, f"test_{timestamp}_screenshot.png")
        driver.save_screenshot(filename)
        print(f"\n[📸] Screenshot saved to: {filename}")
        raise e  # Re-raise to let pytest handle the failure
