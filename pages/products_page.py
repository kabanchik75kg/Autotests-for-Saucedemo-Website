import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .base_page import BasePage


class ProductPage(BasePage):
    """Page Object для страницы товаров."""

    TITLE: tuple[str, str] = (By.CSS_SELECTOR, '[data-test="title"]')
    INVENTORY_LIST: tuple[str, str] = (
        By.CSS_SELECTOR,
        '[data-test="inventory-list"]'
    )
    BURGER_MENU_BUTTON: tuple[str, str] = (By.ID, 'react-burger-menu-btn')
    LOGOUT_SIDEBAR_MENU: tuple[str, str] = (By.ID, 'logout_sidebar_link')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.is_loaded()

    @allure.step("Проверка загрузки страницы товаров")
    def is_loaded(self):
        """Проверяет, что страница товаров загружена."""

        try:
            return (
                self.find_element(self.INVENTORY_LIST).is_displayed() and
                self.find_element(self.TITLE).text == 'Products'
            )
        except Exception:
            return False

    @allure.step("Открытие бокового меню")
    def click_burger_menu_button(self) -> None:
        self.find_element(self.BURGER_MENU_BUTTON).click()

    @allure.step("Нажатие кнопки Logout в меню")
    def click_logout(self) -> None:
        self.find_element(self.LOGOUT_SIDEBAR_MENU).click()

    @allure.step("Выполнение выхода из системы")
    def logout(self) -> 'LoginPage':
        """Выполняет выход и возвращает объект страницы логина."""
        with allure.step("Процесс выхода"):
            self.click_burger_menu_button()
            self.click_logout()

        from .login_page import LoginPage
        return LoginPage(self.driver, False)
