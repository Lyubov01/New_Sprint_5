from data import Data
from locators import Header, RegisterForm, ForgotForm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import wait


def test_login_from_main(browser):
    browser.get(Data.Burger_url)
    wait(browser, Header.login_button).click()
    assert wait(browser, Header.title_form).text == "Вход"


def test_login_from_account_button(browser):
    browser.get(Data.Burger_url)
    wait(browser, Header.My_account).click()
    assert wait(browser, Header.title_form).text == "Вход"


def test_login_from_register_form(browser):
    browser.get(Data.Burger_url)
    wait(browser, Header.login_button).click()
    wait(browser, Header.link_register).click()
    wait(browser, RegisterForm.to_log_in_link).click()
    assert wait(browser, Header.title_form).text == "Вход"


def test_login_from_forgot_password(browser):
    browser.get(Data.Burger_url)
    wait(browser, Header.login_button).click()
    wait(browser, Header.link_fogot_pasword).click()
    wait(browser, ForgotForm.to_log_in_link).click()
    assert wait(browser, Header.title_form).text == "Вход"
