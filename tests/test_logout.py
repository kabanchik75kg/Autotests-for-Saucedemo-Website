from conftest import LOGIN, PASSWORD
from pages.login_page import LoginPage


def test_logout(driver):
    """Проверка выхода залогиненного пользователя."""

    login_page = LoginPage(driver)
    products_page = login_page.login(LOGIN, PASSWORD)
    assert products_page.is_loaded(), "Страница товаров не загрузилась после входа"
    login_page_after_logout = products_page.logout()
    assert login_page_after_logout.is_loaded(), "Страница логина не загрузилась после выхода"
