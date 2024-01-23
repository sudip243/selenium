from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))


driver.get("https://google.com/") #google chromee open hoia jabe
print(driver.title) #j site open holo tar link deba
driver.close() #browser ta close kora holo
