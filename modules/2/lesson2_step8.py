from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

def func(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser.get(link)
	button = browser.find_element_by_css_selector("[type=\"submit\"]")
	button.click() 
	browser.switch_to.alert.accept() # переход на страницу
	
	value_element = browser.find_element_by_css_selector("#input_value")
	value = int(value_element.text)
	answer = func(value)
	input = browser.find_element_by_css_selector("#answer")
	input.send_keys(answer)
	button = browser.find_element_by_css_selector("[type=\"submit\"]")
	button.click() 

finally:
	time.sleep(5)
	browser.quit()


