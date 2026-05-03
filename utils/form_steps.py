import allure
from selenium.webdriver.common.by import By

@allure.step("Заполнение формы login: {login}, password: {password}")
def fill_login_form(driver, login, password):
    driver.get("https://the-internet.herokuapp.com/login")
    login_input = driver.find_element(By.ID, "username")
    login_input.clear()
    login_input.send_keys(login)

    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(password)

    submit_button = driver.find_element(By.CLASS_NAME, "radius")
    submit_button.click()

