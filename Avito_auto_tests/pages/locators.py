from selenium.webdriver.common.by import By


class Button:
    ADD_TO_FAVORITES_BUTTON = (By.XPATH, "//*[text()='Добавить в избранное']", )
    MY_FAVORITES_BUTTON = (By.NAME, "favorites-filled", )

