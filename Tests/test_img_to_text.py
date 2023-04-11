import unittest
from img_to_text import img_to_text
import cv2
from pathlib import Path
from config import Start_Answer, chars_answer, symbols_answer
from outs import OUT1, OUT2, OUT3, OUT4, OUT5, OUT6


class TestImgToText(unittest.TestCase):
    def test_img(self):
        file = Path('Tests/images/Screenshot from 2023-04-02 22-35-47.png')
        img = cv2.imread(filename=str(file))
        self.assertEqual(img_to_text(img=img, split_chars=chars_answer, split_symbols=symbols_answer), OUT1)

    def test_img1(self):
        file = Path('Tests/images/Screenshot from 2023-04-02 22-39-12.png')
        img = cv2.imread(filename=str(file))
        self.assertEqual(img_to_text(img=img, split_chars=chars_answer, split_symbols=symbols_answer), OUT2)
    
    def test_img2(self):
        file = Path('Tests/images/Screenshot (870).png')
        img = cv2.imread(filename=str(file))
        self.assertEqual(img_to_text(img=img, split_chars=chars_answer, split_symbols=symbols_answer), OUT3)

    def test_img3(self):
        file = Path('Tests/images/Screenshot (864).png')
        img = cv2.imread(filename=str(file))
        self.assertEqual(img_to_text(img=img, split_chars=chars_answer, split_symbols=symbols_answer), OUT4)

    def test_img4(self):
        file = Path('Tests/images/Screenshot (869).png')
        img = cv2.imread(filename=str(file))
        self.assertEqual(img_to_text(img=img, split_chars=chars_answer, split_symbols=symbols_answer), OUT5)
    
    def test_img5(self):
        file = Path('/home/legal/github/ChatGPT_answers/Tests/images/multichoise.png')
        img = cv2.imread(filename=str(file))
        self.assertEqual(img_to_text(img=img, split_chars=chars_answer, split_symbols=symbols_answer), OUT6)

if __name__ == "__main__":
    unittest.main()