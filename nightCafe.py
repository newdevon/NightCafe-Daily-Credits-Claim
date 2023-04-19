#start selenium webdriver and setup Service needed for pyinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import creds

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
#driver.maximize_window()

#Navigate to Nightcafe
import time
driver.get("https://creator.nightcafe.studio/login?view=password-login")
time.sleep(10)

#Enter nightcafe login and password text field
from selenium.webdriver.common.by import By
driver.find_element(By.NAME, "email").send_keys(creds.email)
driver.find_element(By.NAME, "password").send_keys(creds.password)

#Click login
driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[2]/div[2]/div/form/div[2]/div[3]/button').click()
# driver.find_element(By.TAG_NAME, "button").click()

#Click top left inbox notifications button
time.sleep(3)
driver.find_element(By.CLASS_NAME, "css-imrmng").click()

""" CLAIM 5 CREDITS """
time.sleep(5)
#driver.find_element(By.CLASS_NAME, "css-10r9n45").click()
driver.find_element(By.XPATH, '//*[@id="modals"]/div/div[2]/div[3]/div/div[2]/div[2]/button').click()

#Close the browser
time.sleep(3)
driver.close()

driver.stop()