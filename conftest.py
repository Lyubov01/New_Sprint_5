import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generator import gen_login, gen_password
from locators import Header, RegisterForm, AccountPage
from data import Data
from utils import wait

WAIT = 12

@pytest.fixture(scope="function")
def browser():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()

@pytest.fixture(scope="function")
def registered_user(browser):
    email = gen_login("lyubov", "melnikova", 30)
    password = gen_password()

    browser.get(Data.Burger_url + "register")
    wait(browser, RegisterForm.name).send_keys("Lyubov")
    wait(browser, RegisterForm.email_in_register_form).send_keys(email)
    wait(browser, RegisterForm.password_in_register_form).send_keys(password)
    wait(browser, RegisterForm.button_to_register).click()

    browser.get(Data.Burger_url + "login")
    wait(browser, Header.email).send_keys(email)
    wait(browser, Header.password).send_keys(password)
    WebDriverWait(browser, WAIT).until(EC.element_to_be_clickable(Header.butoon_log_in)).click()

    WebDriverWait(browser, WAIT).until(
        lambda d: d.execute_script("return !!window.localStorage.getItem('accessToken');"))

    WebDriverWait(browser, WAIT).until(EC.element_to_be_clickable(Header.My_account)).click()
    WebDriverWait(browser, WAIT).until(EC.url_contains("/account"))
    WebDriverWait(browser, WAIT).until(EC.visibility_of_element_located(AccountPage.button_log_out))

    yield browser