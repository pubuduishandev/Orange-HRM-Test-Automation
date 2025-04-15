import pytest
from PageObjects.HomePage import HomePage

@pytest.mark.order(1)
def test_home_page_title(driver):
    home_page = HomePage(driver)
    home_page.load()
    assert "OrangeHRM" in driver.title