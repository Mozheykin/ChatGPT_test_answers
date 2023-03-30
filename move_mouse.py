import pyautogui


def move_mouse(x:int, y:int, w:int, h:int) -> set:
    x = int(x + (w / 2))
    y = int(y + (h / 2))
    pyautogui.position()
    pyautogui.moveTo(x=x, y=y, duration=1)
    return {x, y}
