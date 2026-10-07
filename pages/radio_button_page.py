from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class RadioButtonPage(BasePage):
    URL = "https://formy-project.herokuapp.com/radiobutton"
    RADIO_2 = (By.CSS_SELECTOR, "input[value='option2']")

    def select_radio_2(self):
        self.open_url(self.URL)
        radio = self.wait.until(EC.element_to_be_clickable(self.RADIO_2))
        radio.click()
        return radio.is_selected()