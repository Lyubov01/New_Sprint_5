from generator import gen_login, gen_password
from locators import Header, RegisterForm 
from data import Data
from utils import wait
from data import Text

class TestRegistration:
    def test_success_registration(self, browser):
        browser.get(Data.Burger_url)
        wait(browser, Header.login_button).click()
        wait(browser, Header.link_register).click()

        email = gen_login("lyubov", "melnikova", 30)
        password = gen_password()

        wait(browser, RegisterForm.name).send_keys("Lyubov")
        wait(browser, RegisterForm.email_in_register_form).send_keys(email)
        wait(browser, RegisterForm.password_in_register_form).send_keys(password)
        wait(browser, RegisterForm.button_to_register).click()

        assert wait(browser, Header.title_form).text == Text.login_title_form


    def test_error_short_password(self, browser):
        browser.get(Data.Burger_url)
        wait(browser, Header.login_button).click()
        wait(browser, Header.link_register).click()

        email = gen_login("lyubov", "melnikova", 30)

        wait(browser, RegisterForm.name).send_keys("Lyubov")
        wait(browser, RegisterForm.email_in_register_form).send_keys(email)
        wait(browser, RegisterForm.password_in_register_form).send_keys("123")
        wait(browser, RegisterForm.button_to_register).click()

        assert "Пароль" in wait(browser, RegisterForm.error_mes).text