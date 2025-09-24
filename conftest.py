import pytest
from selenium import webdriver
from generator import gen_login, gen_password
from locators import Header, RegisterForm
from data import Data
from utils import wait


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def registered_user(browser):
    browser.get(Data.Burger_url)
    wait(browser, Header.login_button).click()
    wait(browser, Header.link_register).click()

    email = gen_login("lyubov", "melnikova", 30)
    password = gen_password()

    wait(browser, RegisterForm.name).send_keys("Lyubov")
    wait(browser, RegisterForm.email_in_register_form).send_keys(email)
    wait(browser, RegisterForm.password_in_register_form).send_keys(password)
    wait(browser, RegisterForm.button_to_register).click()

    wait(browser, Header.title_form)
    wait(browser, Header.email).send_keys(email)
    wait(browser, Header.password).send_keys(password)
    wait(browser, Header.butoon_log_in).click()

    yield browser