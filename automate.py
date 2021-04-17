from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
#define driver
driver = webdriver.Chrome()
#initial address
driver.get("https://youtube.com")
#find element on page and send keys
elem = driver.find_element_by_id("search")
elem.send_keys("willcookie")
elem.send_keys(Keys.RETURN)
#Fake actually clicking on result because it wasnt being located
sleep(2)
driver.get("https://www.youtube.com/channel/UCEuGEzTPUJDJL3mOZdwBIWQ")
#Smash that subscribe button
elem = driver.find_element_by_id("subscribe-button")
elem.click()

