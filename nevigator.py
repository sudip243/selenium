from selenium import webdriver
from selenium.webdriver.common.by import By  # locator by use korar jonno locator by use hoiache
from selenium.webdriver.chrome.options import Options # jate chrome browser ta onk khon thake
options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome()
driver.get("https://codejika.org/")
#driver.find_element(By.ID, "3829ed9").click()  #by id selection
#driver.find_element(By.NAME, "3829ed9").click() #by name selection
#driver.find_element(By.CLASS_NAME, "3829ed9").click() #by class name selection
driver.find_element(By.LINK_TEXT, "Start Coding!").click()
#driver.find_element(By.XPATH, "//input[@id='name']").send_keys("sudipto") #value send kore
#driver.find_element(By.XPATH, "//input[@id='name']").clear()#natun value pathanor jonno clear korbo
#driver.find_element(By.XPATH, "//input[@id='name']").send_keys("rahul") #nameun value rahul pathano holo
#input_filed=driver.find_element(By.XPATH, "//input[@id='name']") #bar bar same xpath use korar bodole input_field  name variable baniya naua holo
#input_filed.send_keys("tanmay")
#input_filed.clear()
#input_filed.send_keys("bibhas")
textstore = driver.find_element(By.XPATH, "//a[text()='Skip to content']")
textstore_text=textstore.txt #text the copy hoia store hoia jabe
print(textstore_text)  #text ta print korbe
