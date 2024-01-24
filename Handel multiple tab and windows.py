import time

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()
#driver.implicitly_wait(5) #maxium koto second wait korbe
# get google.co.in
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.window_handles)
driver.find_element(By.ID,'openwindow').click() #natun windows khullo
time.sleep(4)

print(driver.window_handles)

driver.find_element(By.ID,'opentab').click()
time.sleep(3)
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1]) #handeler laganor fole control ta second tab thake tobei open_by_windows er kache galo
driver.find_element(By.XPATH,"//div[@id]//a[(text()='Blog')]").click() #natun windows er blog button e click korlam