import os

from pages.base_page import BasePage
from pages.locators import Button
from selenium.webdriver.common.by import By


class AdPage(BasePage):
    def __init__(self, id_ad: int ):
        base_url = os.getenv("BASE_URL") or "https://avito.ru/"
        super().__init__(base_url)

        self.id = id_ad

        self.open_page(f"{self.url}{id_ad}")

        self.__button_add_favorites = self.driver.find_element(*Button.ADD_TO_FAVORITES_BUTTON)
        self.__button_my_favorites = self.driver.find_element(*Button.MY_FAVORITES_BUTTON)

    def call_button_add_favorites(self):
        self.__button_add_favorites.click()

    def call_button_my_favorites(self):
        self.__button_my_favorites.click()

    def find_ad_after_add(self) -> bool:
        result = self.driver.find_elements(By.XPATH, f"//div[@data-marker=\"item-{self.id}\"]")
        if len(result) == 1:
            return True

        return False


