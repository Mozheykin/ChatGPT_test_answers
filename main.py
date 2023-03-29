import keyboard
from get_screen import screenshot
from img_to_text import img_to_text
from parse_screen_nurseslabs import get_question, get_answers
from loguru import logger
from config import Start_Question, End_Question, Start_Answer, End_Answer

logger.add('logging.log', format='{time} {level} {message}', level='INFO')

def init_press_v():
    logger.info('Get started')
    img = screenshot()
    if img is not None:
        logger.info('Screenshot taken')
        list_text_ocr, positions_answers = img_to_text(img=img, split=Start_Answer)
        logger.info('Get no parse text out image')
        logger.info(f'Positions: {positions_answers}')
        question = get_question(list_text_ocr)
        if question is None:
            raise Exception('get_question return None')
        logger.info(f'[QUESTION] {question}')
        answers = get_answers(list_text_ocr)
        logger.info(f'[ANSWERS] {answers}')
    else:
        raise Exception('NotScreenShotImage')

def main():
    try:
        keyboard.add_hotkey('v', init_press_v)
        keyboard.wait('esc')
    except KeyboardInterrupt:
        logger.info('Script stoped Ctrl+C')
    finally:
        logger.info('Exit')


if __name__ == "__main__":
    main()