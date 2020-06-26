from selenium import webdriver
import time
import unittest

browser = webdriver.Chrome()

def register(url):
    browser.get(url)
    
    # Заполняю обязательные поля
    input1 = browser.find_element_by_css_selector("div.first_block > div > input.first")
    input1.send_keys("a")
    input2 = browser.find_element_by_css_selector("div.first_block > div > input.second")
    input2.send_keys("a")
    input3 = browser.find_element_by_css_selector("div.first_block > div > input.third")
    input3.send_keys("a")
    
    # Отправляю заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    # Проверяем, что смогли зарегистрироваться - ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    regSuccess_text = browser.find_element_by_tag_name("h1").text
    return regSuccess_text

class TestRun(unittest.TestCase):
    def test_one(self):
        url = "http://suninjuly.github.io/registration1.html"
                
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(register(url), "Congratulations! You have successfully registered!", "First test failed to match expected result")
    
    def test_two(self):
        url = "http://suninjuly.github.io/registration2.html"

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(register(url), "Congratulations! You have successfully registered!", "Second test failed to match expected result")

if __name__ == "__main__":
    try:
        unittest.main()
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
    finally:
        browser.quit()