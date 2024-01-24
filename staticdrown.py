# Python program to demonstrate
# selenium
import time

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# create webdriver object
driver = webdriver.Chrome()
# get google.co.in
driver.get("https://www.ironspider.ca/forms/dropdowns.htm")
static_dropdown = driver.find_element(By.XPATH, "//select[@name='coffee']")
select = Select(static_dropdown)
select.select_by_index(2)
time.sleep(5)
select.select_by_visible_text("Black")
time.sleep(5)
select.select_by_value("sugar")
