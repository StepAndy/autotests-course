from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def func(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)
	WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
	book = browser.find_element_by_id("book")
	book.click()
	input_value = browser.find_element_by_id("input_value").text
	value = func(int(input_value))
	input = browser.find_element_by_id("answer")
	input.send_keys(value)
	submit = browser.find_element_by_id("solve")
	submit.click()
finally:
	time.sleep(4)
	browser.quit()

