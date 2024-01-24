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
deal_banners = driver.find_elements(By.XPATH, "//div[@data-clone='false']//a")
print(f"total number of deals: {len(deal_banners)}")  #koto gulo banner ache show korbe
for deal_banner in deal_banners:
    print(deal_banner.get_attribute("href"))  #sob kota banner er link chole asbe
