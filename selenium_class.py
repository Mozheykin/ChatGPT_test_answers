from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# https://chromedriver.chromium.org/help/chrome-doesn-t-start

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

try:
    driver.maximize_window()
    driver.get('https://nurseslabs.com/nursing-pharmacology-nclex-practice-questions-test-bank/')
    time.sleep(5)
    Questions = driver.find_elements(By.CLASS_NAME, 'wpProQuiz_question_text')
    for question in Questions:
        if not question == '':
            text = question.text
            text = text.strip()
            pprint(text)
    # Answers = driver.find_elements(By.CLASS_NAME, 'wpProQuiz_questionInput')
    # for answer in Answers:
    #     pprint(answer.tag_name)
    # button = driver.find_element(By.NAME, 'check')
    # button.send_keys(Keys.ARROW_DOWN)
    # with open('temp.hml', 'w') as file:
    #     file.write(driver.page_source)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
