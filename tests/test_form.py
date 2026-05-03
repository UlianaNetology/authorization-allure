from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import allure
from utils.form_steps import fill_login_form


@allure.epic('Авторизация')
@allure.feature('Проверка двух сценариев авторизации пользователя')

class TestAuthorization():
    @pytest.fixture
    def driver(TestAuthorization):
        # Selenium Manager will auto-download the appropriate driver
        options = Options()
        options.add_argument("--headless")  # run without UI
        options.add_argument("--no-sandbox")  # required in many CI environments
        options.add_argument("--disable-dev-shm-usage")  # overcome limited /dev/shm size on Linux
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    @allure.title('Успешная авторизация')
    @allure.description(
        'Форма авторизации заполняется валидными данными и после нажатия на кнопку "login" отображается приветствие.')
    def test_successful_login(self, driver, get_valid_login_and_password):
        login, password = get_valid_login_and_password
        fill_login_form(driver, login, password)
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div > h4"))
        )
        assert "Welcome to the Secure Area. When you are done click logout below." in success_message.text
        allure.attach(
            driver.get_screenshot_as_png(),
            name="скриншот успешной  авторизации",
            attachment_type=allure.attachment_type.PNG
        )

    @allure.title('Ошибка авторизации')
    @allure.description(
        'Форма авторизации заполняется не валидными данными и после нажатия на кнопку "login" отображается ошибка')
    def test_unsuccessful_login(self, driver, get_invalid_login_and_password):
        login, password = get_invalid_login_and_password
        fill_login_form(driver, login, password)
        success_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#flash")))
        assert "Your username is invalid!" in success_message.text
        allure.attach(
            driver.get_screenshot_as_png(),
            name="скриншот  не успешной  авторизации",
            attachment_type=allure.attachment_type.PNG
        )

