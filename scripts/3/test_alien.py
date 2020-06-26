import pytest
from selenium import webdriver
import time
import math

#В тестовый метод передается фикстура browser
        
@pytest.mark.parametrize('lesson',[236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
class TestMessage:
        def test_alien(self, browser, lesson):
            link = f"https://stepik.org/lesson/{lesson}/step/1"
            browser.get(link)
            browser.implicitly_wait(50)
            input = browser.find_element_by_css_selector("[placeholder='Напишите ваш ответ здесь...']")
            answer = math.log(int(time.time())+0.052)  
            input.send_keys(str(answer))
            button = browser.find_element_by_css_selector(".submit-submission") 
            button.click()
            actual_result = browser.find_element_by_css_selector(".smart-hints__hint").text
            expected_result = "Correct!"
            assert actual_result == expected_result, f"Text mismatch in lesson {lesson}"
            
            