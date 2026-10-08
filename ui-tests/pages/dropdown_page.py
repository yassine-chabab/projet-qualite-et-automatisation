from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DropdownPage(BasePage):
    URL = "https://formy-project.herokuapp.com/dropdown"
    DROPDOWN_BTN = (By.ID, "dropdownMenuButton")
    AUTOCOMPLETE_OPTION = (By.XPATH, "//div[@class='dropdown-menu show']//a[text()='Autocomplete']")

    def select_autocomplete_option(self):
        self.open_url(self.URL)
        self.click(self.DROPDOWN_BTN)
        self.click(self.AUTOCOMPLETE_OPTION)