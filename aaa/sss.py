import selenium,time
from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys(u"haha哈哈")
time.sleep(4)
print(u"我爱你python")
#