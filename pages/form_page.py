from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FormPage(BasePage):
    URL = "https://formy-project.herokuapp.com/form"
    
    # Locateurs
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    JOB_TITLE = (By.ID, "job-title")
    EDUCATION_GRAD = (By.ID, "radio-button-3")
    SEX_MALE = (By.ID, "checkbox-1")
    SUBMIT_BTN = (By.XPATH, "//a[contains(text(),'Submit')]")
    SUCCESS_ALERT = (By.CLASS_NAME, "alert-success")

    def fill_and_submit(self, first_name, last_name, job):
        self.open_url(self.URL)
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.JOB_TITLE, job)
        self.click(self.EDUCATION_GRAD)
        self.click(self.SEX_MALE)
        self.click(self.SUBMIT_BTN)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_ALERT)