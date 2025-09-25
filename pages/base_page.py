from abc import ABC, abstractmethod

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage(ABC):
    '''Абстрактный базовый класс для всех страниц.'''

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.base_url: str = 'https://www.saucedemo.com/'

    @allure.step("Открытие страницы")
    def open(self, url: str = '') -> None:
        """Открывает указанную страницу или базовый URL."""
        target_url = url if url else self.base_url
        with allure.step(f"Переход по URL: {target_url}"):
            self.driver.get(target_url)

    @allure.step("Поиск элемента: {locator[0]} = '{locator[1]}'")
    def find_element(self, locator: tuple[str, str]) -> WebElement:
        """Базовый поиск элемента."""
        return self.driver.find_element(*locator)

    @abstractmethod
    def is_loaded(self):
        """Абстрактный метод проверки загрузки страницы."""

        pass
