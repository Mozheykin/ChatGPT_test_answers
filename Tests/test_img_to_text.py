import unittest
from img_to_text import img_to_text
import cv2
from pathlib import Path
from config import Start_Answer
from pprint import pprint
from outs import OUT1, OUT2, OUT3


class TestImgToText(unittest.TestCase):
    def test_img(self):
        file = Path('Tests/images/Screenshot from 2023-04-02 22-35-47.png')
        img = cv2.imread(filename=str(file))
        pprint(img_to_text(img, Start_Answer))
        self.assertEqual(img_to_text(img, Start_Answer), OUT1)

    def test_img1(self):
        file = Path('Tests/images/Screenshot from 2023-04-02 22-39-12.png')
        img = cv2.imread(filename=str(file))
        pprint(img_to_text(img, Start_Answer))
        self.assertEqual(img_to_text(img, Start_Answer), OUT2)
    
    def test_img2(self):
        file = Path('Tests/images/Screenshot (870).png')
        img = cv2.imread(filename=str(file))
        pprint(img_to_text(img, Start_Answer))
        self.assertEqual(img_to_text(img, Start_Answer), OUT3)

if __name__ == "__main__":
    unittest.main()