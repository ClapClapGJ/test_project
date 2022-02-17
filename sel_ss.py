from selenium import webdriver
import time

driver = webdriver.Chrome()

web = [
    'https://www.google.ru/',
    'https://www.youtube.com/']

for i in range(0, len(web)):
    driver.get(web[i])
    driver.get_screenshot_as_file('screen' + str(i) + '.png')
    time.sleep(2)

driver.quit()
