from selenium import webdriver
import time

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
	browser.get(link)
	button = browser.find_element_by_css_selector("[type=\"submit\"]")
	button.click() 
	browser.switch_to.alert.accept() # переход на страницу
	
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


