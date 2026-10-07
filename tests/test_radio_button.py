import allure
from pages.radio_button_page import RadioButtonPage

@allure.feature("UI Tests - Formy Project")
@allure.story("Sélection Bouton Radio")
def test_radio_button_selection(driver):
    radio_page = RadioButtonPage(driver)
    is_selected = radio_page.select_radio_2()
    
    assert is_selected is True