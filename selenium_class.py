from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import time

# https://chromedriver.chromium.org/help/chrome-doesn-t-start



class SeleniumParse:
    def __init__(self, options_arguments:list, url:str) -> None:
        chrome_options = Options()
        for option in options_arguments:
            chrome_options.add_argument(option)
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        self.driver.maximize_window()
        try:
            self.driver.get(url)
            self.action = ActionChains(self.driver)
        except Exception as ex:
            print(ex)
            self.driver.close()
            self.driver.quit()

    def get_class_text(self, class_names:list):
        try:
            result = dict()
            for class_name in class_names:
                # self.wait_until_visible(class_name=class_name)
                result[class_name] = self.get_find_elements(class_name)
            return result
        except Exception as ex:
            print(ex)
            self.driver.close()
            self.driver.quit()
        
    def wait_until_clickable(self, xpath :str=None, css_selector=None, class_name :str=None, _id :str=None, duration :int=10000, frequency :float=0.01):
        if xpath:
            WebDriverWait(self.driver, duration, frequency).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        elif class_name:
            WebDriverWait(self.driver, duration, frequency).until(EC.element_to_be_clickable((By.CLASS_NAME, class_name)))
        elif css_selector:
            WebDriverWait(self.driver, duration, frequency).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        elif _id:
            WebDriverWait(self.driver, duration, frequency).until(EC.element_to_be_clickable((By.ID, _id)))
    
    def wait_until_visible(self, xpath :str=None, css_selector=None, class_name :str=None, _id :str=None, duration :int=10000, frequency :float=0.01):
        if xpath:
            WebDriverWait(self.driver, duration, frequency).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        elif class_name:
            WebDriverWait(self.driver, duration, frequency).until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
        elif css_selector:
            WebDriverWait(self.driver, duration, frequency).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
        elif _id:
            WebDriverWait(self.driver, duration, frequency).until(EC.visibility_of_element_located((By.ID, _id)))
        
    def get_find_elements(self, class_name:str) -> list:
        elements= self.driver.find_elements(By.CLASS_NAME, class_name)
        result = list()
        for element in elements:
            text = element.text.strip()
            if text:
                result.append(text)
        return result

    def find_element(self, xpath:str=None, partial_link_text:str=None, css_selector:str=None) -> WebElement:
        if xpath:
            return self.driver.find_element(By.XPATH, xpath)
        elif partial_link_text:
            return self.driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text)
        elif css_selector:
            return self.driver.find_element(By.CSS_SELECTOR, css_selector)
    
    def scroll_element(self, element:WebElement):
        self.action.move_to_element(element).perform()
        self.action.click()

        

    def close(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    options_arguments = ['--no-sandbox', '--disable-dev-shm-usage']
    url = 'https://nurseslabs.com/nursing-pharmacology-nclex-practice-questions-test-bank/'
    test_parse = SeleniumParse(options_arguments=options_arguments, url=url)
    text = test_parse.driver.page_source
    with open('temp.html', 'w') as file:
        file.writelines(text)
    # question_class = 'wpProQuiz_question_text'
    # answers_class = 'wpProQuiz_questionListItem'
    # class_names = [question_class, answers_class]

    # result = test_parse.get_class_text(url=url, class_names=class_names)
    # print(f'{result=}')

    # # test_parse.wait_until_clickable(xpath='//*[@id="wpProQuiz_62"]') 
    # button = test_parse.find_element(xpath='//*[@id="wpProQuiz_62"]')
    # test_parse.scroll_element(element=button)

    # index_answer = 3
    # select_answer = test_parse.find_element(xpath=f'//input[@value="{index_answer}"]')
    # # select_answer = select_answer.find_element(By.XPATH, result[answers_class][1])
    # if select_answer:
    #     test_parse.wait_until_clickable(xpath=f'//input[@value="{index_answer}"]')
    #     test_parse.scroll_element(select_answer)
    #     select_answer.click()

    time.sleep(15)
    test_parse.close()