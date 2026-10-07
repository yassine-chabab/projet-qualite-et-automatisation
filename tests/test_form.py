import allure
from pages.form_page import FormPage

@allure.feature("UI Tests - Formy Project")
@allure.story("Soumission de formulaire complet")
def test_submit_form(driver):
    form_page = FormPage(driver)
    form_page.fill_and_submit("Yassine", "Chabab", "QA Automation Engineer")
    
    message = form_page.get_success_message()
    assert "The form was successfully submitted!" in message