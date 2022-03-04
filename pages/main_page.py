from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    # заполняем форму и отправляем данные
    def fill_form(self, firstname, lastname, email, phone):
        self.browser.find_element(*MainPageLocators.FIRSTNAME).send_keys(firstname)
        self.browser.find_element(*MainPageLocators.LASTNAME).send_keys(lastname)
        self.browser.find_element(*MainPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*MainPageLocators.PHONE).send_keys(phone)
        self.browser.find_element(*MainPageLocators.BOXPRIVACY).click()
        self.browser.find_element(*MainPageLocators.SEND).click()
