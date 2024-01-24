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
dropdown_options = driver.find_elements("xpath", ("//ul[contains(@class,'_1sFryS _2x2Mmc _3ofZy1')]//a")) #option gulor xpath
for option in dropdown_options:
    print(f"link present in option : {option.get_attribute('href')}")
    print(f"text present in option : {option.text}") #option gulor text gulo print korbe
    # if "headphones" in option.text:
    #     option.click()
    #     break
    # else:
    #     print("headphones not found")
