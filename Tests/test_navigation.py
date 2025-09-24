from data import Data
from locators import Header, AccountPage, Constructor
from utils import wait



def test_open_account(browser):
    browser.get(Data.Burger_url)
    wait(browser, Header.My_account).click()
    assert wait(browser, Header.title_form).text == 'Вход'


def test_go_to_constructor(browser):
    browser.get(Data.Burger_url + "account")
    wait(browser, Header.constructor_link).click()
    assert "burger" in browser.current_url


def test_go_to_logo(browser):
    browser.get(Data.Burger_url + "account")
    wait(browser, Header.logo_Stellar_Burgers).click()
    assert "burger" in browser.current_url


def test_logout(registered_user):
    registered_user.get(Data.Burger_url + "account")
    wait(registered_user, AccountPage.button_log_out).click()
    assert wait(registered_user, Header.title_form).text == "Вход"


def test_constructor_tabs(browser):
    browser.get(Data.Burger_url)
    wait(browser, Constructor.Burger_name).click()
    wait(browser, Constructor.Souse_name).click()
    wait(browser, Constructor.filling).click()
    
    assert wait(browser, Constructor.filling).is_displayed()
