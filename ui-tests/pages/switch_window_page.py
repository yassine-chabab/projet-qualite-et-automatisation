from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class SwitchWindowPage(BasePage):
    URL = "https://formy-project.herokuapp.com/switch-window"
    ALERT_BTN = (By.ID, "alert-button")

    def trigger_alert_and_get_text(self):
        self.open_url(self.URL)
        self.click(self.ALERT_BTN)
        
        # Attente et gestion du pop-up JS
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()  # Ferme le pop-up en cliquant OK
        return alert_text