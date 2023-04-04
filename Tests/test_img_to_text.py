import unittest
from img_to_text import img_to_text
import cv2
from pathlib import Path
from config import Start_Answer
from outs import OUT1, OUT2, OUT3, OUT4, OUT5


class TestImgToText(unittest.TestCase):
    def test_img(self):
        file = Path('Tests/images/Screenshot from 2023-04-02 22-35-47.png')
        img = cv2.imread(filename=str(file))
        self.assertEqual(img_to_text(img, Start_Answer), OUT1)

    def test_img1(self):
        file = Path('Tests/images/Screenshot from 2023-04-02 22-39-12.png')
        img = cv2.imread(filename=str(file))
        self.assertEqual(img_to_text(img, Start_Answer), OUT2)
    
    def test_img2(self):
        file = Path('Tests/images/Screenshot (870).png')
        img = cv2.imread(filename=str(file))
        self.assertEqual(img_to_text(img, Start_Answer), OUT3)

    def test_img3(self):
        file = Path('Tests/images/Screenshot (864).png')
        img = cv2.imread(filename=str(file))
        self.assertEqual(img_to_text(img, Start_Answer), OUT4)

    def test_img4(self):
        file = Path('Tests/images/Screenshot (869).png')
        img = cv2.imread(filename=str(file))
        self.assertEqual(img_to_text(img, Start_Answer), OUT5)

if __name__ == "__main__":
    unittest.main()