from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# read the username and password from the text file
file = open("schedule.txt", "r")
email = file.readline().rstrip()
password = file.readline().rstrip()
file.close()

# inputs the username, password, and classes to be scheduled into the FlexiSCHED website
driver = webdriver.Chrome()

# oAuth here ↓
driver.get("")

email_input = driver.find_element(By.XPATH, "//input[@id='identifierId']")
email_input.send_keys(email + Keys.RETURN)
sleep(2)
password_input = driver.find_element(By.XPATH, "//input[@name='password']")
password_input.send_keys(password + Keys.RETURN)

sleep(5)
driver.quit()
