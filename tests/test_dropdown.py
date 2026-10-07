import allure
from pages.dropdown_page import DropdownPage

@allure.feature("UI Tests - Formy Project")
@allure.story("Sélection dans Liste Déroulante")
def test_select_dropdown_item(driver):
    dropdown_page = DropdownPage(driver)
    dropdown_page.select_autocomplete_option()
    
    assert "/autocomplete" in driver.current_url