import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/konda/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(15)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#driver.find_element(By.CLASS_NAME, "oxd-icon bi-chevron-right").click()
driver.find_element(By.LINK_TEXT, "PIM").click()
driver.find_element(By.LINK_TEXT, "Employee List").click()
time.sleep(5)
name_list = driver.find_elements(By.XPATH,"//div[@class='oxd-table-cell oxd-padding-cell'][3]/child::div")
my_list = []

for name in name_list:
    my_list.append(name.text)
print(my_list)




