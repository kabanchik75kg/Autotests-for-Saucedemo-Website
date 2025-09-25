from conftest import LOGIN, PASSWORD
from pages.login_page import LoginPage
from pages.products_page import ProductPage


def test_login(driver):
    """Проверка успешного входа зарегистрированного пользователя."""

    login_page = LoginPage(driver)
    products_page = login_page.login(LOGIN, PASSWORD)

    assert products_page.is_loaded()
