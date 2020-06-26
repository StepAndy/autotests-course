import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
	browser = webdriver.Chrome()
	browser.get(link)
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	input = browser.find_element_by_id("answer")
	input.send_keys(y)
	check_box = browser.find_element_by_id("robotCheckbox")
	check_box.click()
	radio_button = browser.find_element_by_id("robotsRule")
	radio_button.click()
	submit = browser.find_element_by_css_selector("[type=\"Submit\"]")
	submit.click()
	
finally:
	time.sleep(4)
	browser.quit()
	
