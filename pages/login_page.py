import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .base_page import BasePage


class LoginPage(BasePage):
    """Page Object для страницы входа."""

    USERNAME: tuple[str, str] = (By.CSS_SELECTOR, '[data-test="username"]')
    PASSWORD: tuple[str, str] = (By.CSS_SELECTOR, '[data-test="password"]')
    LOGIN_BUTTON: tuple[str, str] = (
        By.CSS_SELECTOR,
        '[data-test="login-button"]'
    )

    def __init__(self, driver: WebDriver, open_page: bool = True) -> None:
        super().__init__(driver)
        if open_page:
            self.open()
        self.is_loaded()

    @allure.step("Проверка загрузки страницы логина")
    def is_loaded(self) -> bool:
        """Проверяет, что страница логина загружена."""

        try:
            is_loaded = (
                self.find_element(self.LOGIN_BUTTON).is_displayed() and
                self.find_element(self.USERNAME).is_displayed() and
                self.find_element(self.PASSWORD).is_displayed()
            )
            allure.dynamic.description(f"Страница логина загружена: {is_loaded}")
            return is_loaded
        except Exception:
            return False

    @allure.step("Ввод логина: {username}")
    def enter_username(self, username: str) -> None:
        self.find_element(LoginPage.USERNAME).send_keys(username)

    @allure.step("Ввод пароля")
    def enter_password(self, password: str) -> None:
        self.find_element(LoginPage.PASSWORD).send_keys(password)

    @allure.step("Нажатие кнопки Login")
    def click_login_button(self) -> None:
        self.find_element(LoginPage.LOGIN_BUTTON).click()

    @allure.step("Выполнение входа пользователя {username}")
    def login(self, username: str, password: str) -> 'ProductPage':
        """Выполняет логин и возвращает объект страницы ProductPage."""
        with allure.step("Процесс аутентификации"):
            self.enter_username(username)
            self.enter_password(password)
            self.click_login_button()

        from .products_page import ProductPage
        return ProductPage(self.driver)
