# Python program to demonstrate
# selenium
import time

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()
# get google.co.in
driver.get("https://www.ironspider.ca/forms/checkradio.htm")
blinking_link = driver.find_element(By.XPATH, "//a[text()='Free Text Editors']")
print(blinking_link.get_attribute("title"))

