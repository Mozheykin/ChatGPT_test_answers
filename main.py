import keyboard
from get_screen import screenshot
from img_to_text import img_to_text
from parse_screen_nurseslabs import get_question, get_answers, get_nltk_index, get_answer_text, get_question_text
from chatgpt import get_response, get_answer
from loguru import logger
from config import Start_Question, End_Question, Start_Answer, End_Answer, chars_answer, symbols_answer
from move_mouse import move_mouse
from errors import *
from time import sleep

logger.add('logging.log', format='{time} {level} {message}', level='INFO')

MAIN_URL = 'https://nurseslabs.com/nursing-pharmacology-nclex-practice-questions-test-bank/'

def select_true_answer(index:int, positions_answers):
    select = positions_answers[index]
    x, y = move_mouse(x=select.get('x'), y=select.get('y'), w=select.get('w'), h=select.get('h'))
    logger.info(f'{x=}, {y=}')

def init_press_v():
    try:
        logger.info('Get started')
        img = screenshot()
        if img is not None:
            logger.info('Screenshot taken')

            list_text_ocr, positions_answers = img_to_text(img=img, split_chars=chars_answer, split_symbols=symbols_answer)
            logger.info('Get no parse text out image')
            logger.info(f'Positions: {positions_answers}')
            if any([not positions_answers, positions_answers is None]):
                raise NotParsePositionAnswer('Not parse positions answers')

            question = get_question_text(list_text_ocr)
            if question is None:
                raise GetQuestionReturnNone('get_question return None')
            logger.info(f'[QUESTION] {question}')

            answers = get_answer_text(list_text_ocr)
            logger.info(f'[ANSWERS] {answers}')
            if answers is None:
                raise GetAnswersReturnNone('get_answers return None')
            
            if len(positions_answers) < len(answers):
                length_answers = len(positions_answers)
                print(answers)
                answers = answers[-length_answers:]
                print(answers)

            request = f'Question: {question}, Options: {" ".join(answer for answer in answers)}'
            response = get_response(request=request)
            logger.info(f'Response: {response}')
            answer_chatgpt = get_answer(response=response)
            logger.info(f'Answer: {answer_chatgpt}')
            if response is None:
                raise GetResponseReturnNone('get_response return None')
            if answer_chatgpt is None:
                raise GetAnswerReturnNone('get_answer return None')

            nltk_list = get_nltk_index(answer_gpt=answer_chatgpt, answers=answers)
            logger.info(f'nltk: {nltk_list}')
            for nltk in nltk_list:
                index = nltk.index(max(nltk)) + 1
                select_true_answer(index, positions_answers)

        else:
            raise Exception('NotScreenShotImage')
        
    except NotParsePositionAnswer as ex:
        logger.error(f'Exception: {ex}')
    except GetQuestionReturnNone as ex:
        logger.error(f'Exception: {ex}')
    except GetAnswersReturnNone as ex:
        logger.error(f'Exception: {ex}')
    except GetResponseReturnNone as ex:
        logger.error(f'Exception: {ex}')
    except GetAnswerReturnNone as ex:
        logger.error(f'Exception: {ex}')

def main():
    try:
        keyboard.add_hotkey('v', init_press_v)
        keyboard.wait('esc')
    except KeyboardInterrupt:
        logger.info('Script stoped Ctrl+C')
    except Exception as ex:
        logger.error(f'error: {ex}')
    finally:
        logger.info('Exit')


if __name__ == "__main__":
    main()