from pathlib import Path
from img_to_text import img_to_text
import cv2
from config import Start_Answer
from pprint import pprint

file = Path('Tests/images/Screenshot (869).png')
img = cv2.imread(filename=str(file))
pprint(img_to_text(img, Start_Answer))