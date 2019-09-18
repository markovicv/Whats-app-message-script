from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/home/vukasin/chromiumDriver/chromedriver')
driver.get('http://www.google.com')
search = driver.find_element_by_name('q')
search.send_keys("hilti")
search.send_keys(Keys.RETURN)