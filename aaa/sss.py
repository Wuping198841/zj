import selenium,time
from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenuim")
time.sleep(4)
print("1234")
