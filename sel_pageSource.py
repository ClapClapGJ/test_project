from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get("https://stepik.org/lesson/25969/step/8")
#print(driver.page_source)

time.sleep(2)

driver.quit()
