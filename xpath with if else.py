# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()
# get google.co.in
driver.get("https://www.facebook.com/")
# textstore = driver.find_element(By.XPATH, "//a[text()='Skip to content']")
# textstore_text = textstore.text  # text the copy hoia store hoia jabe
# print(textstore_text)
driver.find_element(By.XPATH, "//*[@id='email']").send_keys("sudipto")
driver.find_element(By.XPATH, "//*[@id='email']").clear()
driver.find_element(By.XPATH, "//*[@id='email']").send_keys("rahul")
act_title = driver.title  #variable naua holo jekhane driver title store kora holo
exp_title = "Facebook – log in or sign up" #expected title naua holo page tar
if act_title == exp_title:  #compare kora holo
    print("login test is passed")
else:
    print("login test failed")
