from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions,Chrome
import time



friend = input("chat name: ")
message = input("message: ")

driver = webdriver.Chrome('/home/vukasin/chromiumDriver/chromedriver')
driver.get("https://web.whatsapp.com/")

input("enter any key")

#finds the person you want to send the message
chat = driver.find_element_by_xpath('//span[@title = "{}"]'.format(friend))
chat.click()

#finds the chat box in whatsapp and types the the text yout entered
message_box = driver.find_element_by_class_name("_13mgZ")
message_box.send_keys(message)

#finds the send btn and sends the message to the user
btn_send = driver.find_element_by_class_name("_3M-N-")
btn_send.send_keys(Keys.RETURN)








 