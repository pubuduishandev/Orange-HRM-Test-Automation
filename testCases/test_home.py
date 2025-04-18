import pytest
from PageObjects.HomePage import HomePage
from Utilities.data_loader import load_urls_from_json

# Step 1: Load base URLs from test data JSON
test_urls = load_urls_from_json()

@pytest.mark.order(1)
@pytest.mark.parametrize("url_data", test_urls)
def test_home_page_title(driver, url_data):
    # Step 2: Extract base URL from the current dataset
    base_url = url_data["base_url"]

    # Step 3: Initialize the HomePage object (uses WebDriver instance)
    home_page = HomePage(driver)

    # Step 4: Override the homepage URL with test data (bypasses config)
    home_page.url = base_url

    # Step 5: Navigate to the base URL
    home_page.load()

    # Step 6: Retrieve the current page title
    actual_title = home_page.get_title()

    # Step 7: Define the expected title string for OrangeHRM
    expected_title = "OrangeHRM"

    # Step 8: Compare the actual title with expected title using exact match
    assert actual_title.strip() == expected_title, (
        f"\n[❌] Title mismatch for: {base_url}"
        f"\nExpected: {expected_title}"
        f"\nActual: {actual_title}"
    )
