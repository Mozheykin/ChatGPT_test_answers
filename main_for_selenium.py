from selenium_class import SeleniumParse
import re
from chatgpt import get_answer, get_response
from parse_screen_nurseslabs import get_nltk_index
import time


def get_url() -> str:
    while True:
        url = input("Write url test, or write 'N' to default url: ")
        if url == 'N':
            url = 'https://nurseslabs.com/nursing-pharmacology-nclex-practice-questions-test-bank/'

        validation_url = re.search(r'^((http|https):\/\/)[-a-zA-Z0-9@:%._\\+~#?&\/\/=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%._\\+~#?&\/\/=]*)$', url)
        if validation_url:
            return url
        else:
            print('Not valid url')


def main():
    url = get_url()
    options_arguments = ['--no-sandbox', '--disable-dev-shm-usage']
    core = SeleniumParse(options_arguments=options_arguments, url=url)
    question_class = 'wpProQuiz_question_text'
    answers_class = 'wpProQuiz_questionListItem'
    class_names = [question_class, answers_class]

    while True:
        result = core.get_class_text(class_names=class_names)

        print(result)

        if result[answers_class] and result[question_class]:
            request = f'Question: {result[question_class]}, Options: {" ".join(answer for answer in result[answers_class])}'
            response = get_response(request=request)
            answer_chatgpt = get_answer(response=response)

            print(answer_chatgpt)

            nltk_list = get_nltk_index(answer_gpt=answer_chatgpt, answers= result[answers_class])

            print(nltk_list[0])

            index_answer = nltk_list[0].index(max(nltk_list[0])) + 1
            print(index_answer)

            poligon_question = core.find_element(xpath='//*[@id="wpProQuiz_62"]')
            core.scroll_element(element=poligon_question)

            select_answer = core.find_element(xpath=f'//input[@value="{index_answer}"]')

            if select_answer:
                # core.wait_until_clickable(xpath=f'//input[@value="{index_answer}"]')
                core.scroll_element(select_answer)
                select_answer.click()
            
            # button = core.find_element(xpath='//button[@value="Check"]')
            # if button:
            #     core.scroll_element(element=button)
            #     button.click()
            
            time.sleep(10)
    
    core.close()



if __name__ == '__main__':
    main()