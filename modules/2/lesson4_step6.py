from selenium import webdriver
import time
link = "http://suninjuly.github.io/cats.html"

try:
	browser = webdriver.Chrome()
	browser.find_element_by_id("button")
finally:
	time.sleep(4)
	browser.quit()
