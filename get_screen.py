import pyautogui
from pathlib import Path
from PIL import Image

def screenshot(path:str='', name:str='') -> Image:
    """get screenshot, if path or name true then save image else not save
    Args:
        path (str): path derrictory save
        name (str): name file
    Returns:
        Image: PIL.Image return, or None
    """
    if any([path, name]):
        path_screenshot = Path(path, name)
        path_screenshot.parent.mkdir(parents=True, exist_ok=True)
        return pyautogui.screenshot(path_screenshot)
    else:
        return pyautogui.screenshot()


if __name__ == "__main__":
    screenshot(path='test', name='test.png')