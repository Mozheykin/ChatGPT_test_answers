import pyautogui


def move_mouse(x:int, y:int, w:int, h:int) -> None:
    x = (x + (w / 2))
    y = (y + (h / 2))
    print(f'{x=} {y=}')
    pyautogui.moveTo(x=x, y=y, duration=0.5)
