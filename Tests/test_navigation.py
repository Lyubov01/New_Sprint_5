from data import Data
import pytest
from locators import Header, AccountPage, Constructor
from utils import wait, safe_click, wait_clickable
from data import Text


class TestNavigation:
    def test_open_account(self, browser):
        browser.get(Data.Burger_url)
        wait(browser, Header.My_account).click()
        assert wait(browser, Header.title_form).text == Text.login_title_form


    def test_go_to_constructor(self, browser):
        browser.get(Data.Burger_url + "account")
        wait(browser, Header.constructor_link).click()
        assert "burger" in browser.current_url

    def test_go_to_logo(self, browser):
        browser.get(Data.Burger_url + "account")
        wait(browser, Header.logo_Stellar_Burgers).click()
        assert "burger" in browser.current_url

    def test_logout(self, registered_user):
        registered_user.get(Data.Burger_url + "account")
        safe_click(registered_user, AccountPage.button_log_out)
        assert wait(registered_user, Header.title_form).text == Text.login_title_form


    @pytest.mark.parametrize("tab", [
        Constructor.Burger_name,
        Constructor.Souse_name,
        Constructor.filling])
    def test_constructor_tabs(self, browser, tab):
        browser.get(Data.Burger_url)
        safe_click(browser, tab)
        assert wait_clickable(browser, tab).is_displayed()