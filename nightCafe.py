#start selenium webdriver and setup Service needed for pyinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import creds

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
#driver.maximize_window()

#navigate to Nightcafe
import time
driver.get("https://creator.nightcafe.studio/login?view=password-login")
time.sleep(10)

#enter nightcafe login and password text field
from selenium.webdriver.common.by import By
driver.find_element(By.NAME, "email").send_keys(creds.email)
driver.find_element(By.NAME, "password").send_keys(creds.password)

#click login
driver.find_element(By.TAG_NAME, "button").click()

#click top left inbox notifications button
time.sleep(3)
driver.find_element(By.CLASS_NAME, "css-imrmng").click()

""" CLAIM 5 CREDITS """
time.sleep(5)
#driver.find_element(By.CLASS_NAME, "css-10r9n45").click()
driver.find_element(By.XPATH, '//*[@id="modals"]/div/div[2]/div[3]/div/div[2]/div[2]/button').click()

#close the browser
time.sleep(3)
driver.close()

driver.stop()