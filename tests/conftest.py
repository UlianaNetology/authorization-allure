import allure
import pytest


@pytest.fixture
@allure.step('Подготовка валидных данных')
def get_valid_login_and_password():
    return "tomsmith", "SuperSecretPassword!"


@pytest.fixture
@allure.step('Подготовка не валидных данных')
def get_invalid_login_and_password():
    return "tom", "Super"