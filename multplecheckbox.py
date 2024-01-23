# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()
# get google.co.in
driver.get("https://www.ironspider.ca/forms/checkradio.htm")
check_boxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(check_boxes) #checkbox er details dekhabe list e ese porbe
print(len(check_boxes)) #check box koto gulo ache show korbe
for check_boxe in check_boxes:
    check_boxe.click() #eta dile e sobkota check box por por select hoia jabe
