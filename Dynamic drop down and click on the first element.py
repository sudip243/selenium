# Python program to demonstrate
# selenium
import time

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()
# get google.co.in
driver.get("https://www.flipkart.com/")
search_box = driver.find_element("xpath", "//input[@type='text']")
search_box.send_keys("one plus headphones") #search korbe eta . lekha ta option ta pathano holo
time.sleep(3) #eta na pathale link brake hoia jabe kaorn eato first search kore click korte parbe na
first_option = driver.find_element("xpath", "(//ul[contains(@class,'_1sFryS _2x2Mmc _3ofZy1')]//a)[1]") #first option er xpath
print("link present in first option : {first_option.get_attribute('href')}")
print("text present in first option : {first_option.text}") #first option tar text ta print korbe
first_option.click() #j option ta select ache seta k click korbe
print(driver.current_url) #current link ta print korbe
