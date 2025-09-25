import shutil
from typing import Any

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.remote.webdriver import WebDriver

LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'


def pytest_addoption(parser: Any) -> None:
    """Добавляем кастомные опции командной строки."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "edge"],
        help="Браузер для тестов: chrome, firefox или edge"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск в headless режиме (без графического интерфейса)"
    )


def setup_local_driver(browser: str, headless: bool) -> WebDriver:
    """Настраивает локальный драйвер для выбранного браузера."""

    driver: WebDriver
    if browser == "chrome":
        chrome_options = ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless=new")
        # ОСНОВНОЕ: отключаем проверку утечек пароля
        chrome_options.add_argument('--disable-features=PasswordLeakDetection')

        # Дополнительные настройки
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-save-password-bubble')
        chrome_options.add_argument('--no-first-run')
        chrome_options.add_argument('--no-default-browser-check')
        chrome_options.add_argument('--disable-password-manager-reauthentication')

        # Критически важные настройки для паролей
        chrome_options.add_experimental_option('prefs', {
            'credentials_enable_service': False,
            'profile.password_manager_enabled': False,
            'password_manager_enabled': False,
            'profile.password_manager_leak_detection': False,
        })

        # Расширенные excludeSwitches
        chrome_options.add_experimental_option('excludeSwitches', [
            'enable-automation',
            'enable-logging',
            'disable-popup-blocking',
            'password-manager-reauthentication'
        ])

        # Для максимального отключения безопасности паролей
        chrome_options.add_argument('--disable-backgrounding-occluded-windows')
        chrome_options.add_argument('--disable-renderer-backgrounding')
        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":
        service = Service(shutil.which("geckodriver"))
        firefox_options = FirefoxOptions()
        if headless:
            firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(service=service, options=firefox_options)

    elif browser == "edge":
        edge_options = EdgeOptions()
        if headless:
            edge_options.add_argument("--headless=new")
        driver = webdriver.Edge(options=edge_options)

    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser}")

    return driver


@pytest.fixture()
def driver(request: pytest.FixtureRequest):
    """
    Фикстура для инициализации WebDriver с настройками из командной строки.
    """

    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    driver = None
    try:
        driver = setup_local_driver(browser, headless)
        driver.implicitly_wait(3)
        yield driver
    except Exception as e:
        pytest.fail(f"Не удалось инициализировать WebDriver: {str(e)}")
    finally:
        if driver:
            driver.quit()
