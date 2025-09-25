# Autotests-for-Saucedemo-Website
Проект автоматизированного тестирования для сайта Saucedemo (https://www.saucedemo.com/) с использованием Selenium и pytest.

### Обязательные тесты
**Аутентификация пользователя**: Проверка входа с валидными учетными данными

### Дополнительные тесты
**Выход из системы**: Проверка выхода залогиненного пользователя
**Поддержка разных браузеров**: Chrome, Firefox, Edge
**Headless режим**: Запуск без графического интерфейса
**Allure отчеты**: Детальная визуализация результатов тестирования

## Запуск тестов

### Базовый запуск 
``` pytest tests/ ``` 

### Запуск с выбором браузера
```
pytest tests/ --browser=firefox
pytest tests/ --browser=edge
pytest tests/ --browser=chrome
```
### Headless режим
```
pytest tests/ --headless
pytest tests/ --browser=firefox --headless
```
### Генерация Allure отчетов
```
# Запуск тестов с сохранением результатов
pytest tests/ --alluredir=results

# Просмотр отчета
allure serve allure-results
```

## Технологический стек

- **Python 3.10+** - язык программирования
- **Selenium WebDriver** - автоматизация браузера
- **pytest** - фреймворк для тестирования
- **Allure Framework** - система отчетности
- **Page Object Pattern** - архитектурный паттерн
