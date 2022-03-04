

class BasePage:
    # создаем конструктор
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # метод для открытия браузера
    def open(self):
        self.browser.get(self.url)
