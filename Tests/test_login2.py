from data import Data
from locators import Header, RegisterForm, ForgotForm
from utils import wait
from data import Text


class TestLogin:
    def test_login_from_main(self, browser):
        browser.get(Data.Burger_url)
        wait(browser, Header.login_button).click()
        assert wait(browser, Header.title_form).text == Text.login_title_form

    def test_login_from_account_button(self, browser):
        browser.get(Data.Burger_url)
        wait(browser, Header.My_account).click()
        assert wait(browser, Header.title_form).text == Text.login_title_form


    def test_login_from_register_form(self, browser):
        browser.get(Data.Burger_url)
        wait(browser, Header.login_button).click()
        wait(browser, Header.link_register).click()
        wait(browser, RegisterForm.to_log_in_link).click()
        assert wait(browser, Header.title_form).text == Text.login_title_form


    def test_login_from_forgot_password(self, browser):
        browser.get(Data.Burger_url)
        wait(browser, Header.login_button).click()
        wait(browser, Header.link_fogot_pasword).click()
        wait(browser, ForgotForm.to_log_in_link).click()
        assert wait(browser, Header.title_form).text == Text.login_title_form
