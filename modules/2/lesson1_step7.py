import time
import math
from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html?ruler=robots"

def func(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("[src=\"images/chest.png\"]")
    x = x_element.get_attribute("valuex")
    answer = func(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(answer)
    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()
    robotsRule = browser.find_element_by_id("robotsRule")
    robotsRule.click()
    submit = browser.find_element_by_css_selector("[type=\"submit\"]")
    submit.click()
finally:
    time.sleep(5)
    browser.quit()
    
