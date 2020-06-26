from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/execute_script.html"

def func(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	answer = func(int(x))
	input = browser.find_element_by_id("answer")
	input.send_keys(answer)
	robotCheckbox = browser.find_element_by_id("robotCheckbox")
	robotCheckbox.click()
	submit = browser.find_element_by_css_selector("[type=\"submit\"]")
	browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
	robotsRule = browser.find_element_by_id("robotsRule")
	robotsRule.click()
	submit.click()
finally:
	time.sleep(3)
	browser.quit()
	