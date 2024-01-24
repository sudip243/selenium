# import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()
driver.implicitly_wait(5) #maxium koto second wait korbe
# get google.co.in
driver.get("https://www.flipkart.com/")
search_box = driver.find_element("xpath", "//input[@type='text']")
actions = ActionChains(driver,duration=2000) # mouse er duration bole
actions.move_to_element(driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/div[1]/div/div/span/span[1]")).click().perform() #element tate hober korbe and click korbe
# actions.move_to_element(driver.find_element(By.XPATH,"//a[text()='Women Ethnic']")).click().perform()  #selected element e hober korbe and single click korbe
# actions.move_to_element(driver.find_element(By.XPATH,"//a[text()='Women Ethnic']")).double_click().perform() #selected element e hober korbe and double click korbe
actions.move_to_element(driver.find_element(By.XPATH,"//a[text()='Women Ethnic']")).context_click().perform()  #selected element e hober korbe and right click korbe
