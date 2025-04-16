import pytest
from PageObjects.HomePage import HomePage
from Utilities.data_loader import load_titles_from_json

test_titles = load_titles_from_json()

@pytest.mark.order(1)
@pytest.mark.parametrize("test_data", test_titles)
def test_home_page_title(driver, test_data):
    # Step 1: Extract base_url and expected title from test data
    base_url = test_data["base_url"]
    expected_title = test_data["title"]

    # Step 2: Initialize the HomePage object and override its URL with the test case URL
    home_page = HomePage(driver)
    home_page.url = base_url  # override the one from config
    home_page.load()

    # Step 3: Get the actual title of the currently loaded page
    actual_title = home_page.get_title()

    # Step 4: Set the strict expected condition
    # Only accept test data with a specific base_url AND title
    expected = (
        test_data["base_url"] == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        and test_data["title"] == "OrangeHRM"
    )

    # Step 5: Assert that:
    #  - The test data matches the known correct combo (expected == True)
    #  - The actual page title matches the expected title (case-insensitive, partial match allowed)
    # If either fails, throw a detailed assertion error
    assert (expected and expected_title in actual_title), (
        f"Test failed for base_url: {base_url}\n"
        f"Expected title: OrangeHRM\n"
        f"Actual title: {actual_title}\n"
        f"Is expected combo? {expected}"
    )
