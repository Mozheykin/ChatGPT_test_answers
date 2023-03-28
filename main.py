import keyboard
from get_screen import screenshot
from img_to_text import img_to_text
from pprint import pprint


def init_press_v():
    print('[INFO] Get started')
    img = screenshot()
    if img is not None:
        print('[INFO] Screenshot taken')
        list_text_ocr = img_to_text(img=img)
        # pprint(list_text_ocr)


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