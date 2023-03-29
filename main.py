import keyboard
from get_screen import screenshot
from img_to_text import img_to_text
from pprint import pprint
from parse_screen_nurseslabs import get_question, get_answer


def init_press_v():
    print('[INFO] Get started')
    img = screenshot()
    if img is not None:
        print('[INFO] Screenshot taken')
        list_text_ocr = img_to_text(img=img)
        print('[INFO] Get no parse text out image')
        question = get_question(list_text_ocr)
        if question is None:
            raise Exception('get_question return None')
        print(f'[QUESTION] {question}')



    else:
        raise Exception('NotScreenShotImage')

def main():
    try:
        keyboard.add_hotkey('v', init_press_v)
        keyboard.wait('esc')
    except KeyboardInterrupt:
        print('[INFO] Script stoped Ctrl+C')
    finally:
        print('[INFO] Exit')


if __name__ == "__main__":
    main()