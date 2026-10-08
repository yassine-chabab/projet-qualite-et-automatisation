import allure
from pages.switch_window_page import SwitchWindowPage

@allure.feature("UI Tests - Formy Project")
@allure.story("Gestion des Pop-ups et Alertes JS")
def test_javascript_alert(driver):
    switch_page = SwitchWindowPage(driver)
    alert_text = switch_page.trigger_alert_and_get_text()
    
    
    assert "This is a test alert!" in alert_text