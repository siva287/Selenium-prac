import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/konda/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)

driver.get("https://netbanking.hdfcbank.com/netbanking/")
time.sleep(3)
driver.execute_script("window.scrollBy(100,1000)")
print("scrolled_down")
time.sleep(10)


