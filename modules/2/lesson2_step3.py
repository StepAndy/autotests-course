from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1_element = browser.find_element_by_id("num1")
    num1 = int(num1_element.text)
    num2_element = browser.find_element_by_id("num2")
    num2 = int(num2_element.text)
    summary = num1 + num2
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(summary))
    submit = browser.find_element_by_css_selector("[type=\"submit\"]")
    submit.click()
    
finally:
    time.sleep(2)
    browser.quit()
    
