import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(autouse=True)
def browser():
    driver = Service("Selenium_edukation/chromedriver/")
    pytest.driver = webdriver.Chrome(service=driver)

    # Переходим на страницу авторизации
    pytest.driver.get('https://petfriends.skillfactory.ru/login')

    # Максимизируем окно браузера
    pytest.driver.maximize_window()

    pytest.driver.implicitly_wait(10)

    yield pytest.driver

    pytest.driver.quit()
