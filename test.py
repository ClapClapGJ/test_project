import time
from .pages.main_page import MainPage
from .pages.download_page import DownloadPage


main_page_link = "https://r7-office.ru/request_personal"
download_page_link = "https://r7-office.ru/downloads"


class TestDownloadForm:
    def setup(self):
        self.email = str(time.time()) + "@email.ru"
        self.firstname = "firstname"
        self.lastname = "lastname"
        self.phone = "9999999999"

    def test_can_fill_form(self, browser):
        page = MainPage(browser, main_page_link)
        page.open()
        page.fill_form(firstname=self.firstname, lastname=self.lastname, email=self.email, phone=self.phone)
        time.sleep(3)
        page = DownloadPage(browser, download_page_link)
        page.open()
        page.find_and_safe_text()

