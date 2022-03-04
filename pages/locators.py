from selenium.webdriver.common.by import By


class MainPageLocators:
    FIRSTNAME = (By.NAME, "first_name")
    LASTNAME = (By.NAME, "last_name")
    EMAIL = (By.NAME, "email")
    PHONE = (By.NAME, "tildaspec-phone-part[]")
    SEND = (By.CLASS_NAME, "t-submit")
    BOXPRIVACY = (By.CLASS_NAME, "t-checkbox__control")


class DownloadPageLocators:
   ALT = (By.XPATH, '//*[@id="rec204012169"]/div/div/div[8]/a')
   ROSA = (By.XPATH, '//*[@id="rec204012169"]/div/div/div[9]/a')
   ASTRA = (By.XPATH, '//*[@id="rec204012169"]/div/div/div[10]/a')
   RED = (By.XPATH, '//*[@id="rec204012169"]/div/div/div[11]/a')

   # options.add_argument('--ignore-certificate-errors')
   #     options.add_argument('--ignore-ssl-errors')
   # /html/body/div[1]/div[9]/div/div/div[9]/a



