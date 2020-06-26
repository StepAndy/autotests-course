from selenium import webdriver
import time
import os 

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
current_dir = os.path.abspath(os.path.dirname(__file__))   
file_path = os.path.join(current_dir, 'phones.txt')  

try:
	browser.get(link)
	firstname = browser.find_element_by_css_selector("[name=\"firstname\"]")
	firstname.send_keys("Hello")
	lastname = browser.find_element_by_css_selector("[name=\"lastname\"]")
	lastname.send_keys("World!")
	email = browser.find_element_by_css_selector("[name=\"email\"]")
	email.send_keys("email")
	attach = browser.find_element_by_id("file")
	attach.send_keys(file_path)
	button = browser.find_element_by_css_selector("[type=\"submit\"]")
	button.click()
finally:
	time.sleep(5)
	browser.quit()