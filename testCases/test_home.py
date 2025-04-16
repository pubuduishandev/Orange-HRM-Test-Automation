import pytest
from PageObjects.HomePage import HomePage
from Utilities.data_loader import load_titles_from_json

test_titles = load_titles_from_json()

@pytest.mark.order(1)
@pytest.mark.parametrize("test_data", test_titles)
def test_home_page_title(driver, test_data):
    base_url = test_data["base_url"]
    expected_title = test_data["title"]

    # Initialize HomePage and override the URL
    home_page = HomePage(driver)
    home_page.url = base_url  # override the one from config
    home_page.load()

    actual_title = home_page.get_title()

    # Strict validation logic
    expected = (
        test_data["base_url"] == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        and test_data["title"] == "OrangeHRM"
    )

    # Pass only if the actual title matches AND this is the one expected combo
    assert (expected and expected_title in actual_title), (
        f"Test failed for base_url: {base_url}\n"
        f"Expected title: OrangeHRM\n"
        f"Actual title: {actual_title}\n"
        f"Is expected combo? {expected}"
    )
