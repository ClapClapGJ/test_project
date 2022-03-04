from .base_page import BasePage
from .locators import DownloadPageLocators


class DownloadPage(BasePage):
    # находим название ос и печатаем из списка
    def find_and_safe_text(self):
        alt = self.browser.find_element(*DownloadPageLocators.ALT).text
        rosa = self.browser.find_element(*DownloadPageLocators.ROSA).text
        astra = self.browser.find_element(*DownloadPageLocators.ASTRA).text
        red = self.browser.find_element(*DownloadPageLocators.RED).text
        os_list = [alt,
                   rosa,
                   astra,
                   red
                   ]
        for x in os_list:
            print(x)

