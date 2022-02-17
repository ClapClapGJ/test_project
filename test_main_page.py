from Pages.MainPage import MainPage
from Pages.LoginPage import LoginPage
import time


def test_sch_now(browser):
    link = 'http://jade/130201/'
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.login_jade()
    main_page = MainPage(browser,link)
    main_page.click_ukd()

