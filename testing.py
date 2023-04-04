from pathlib import Path
from img_to_text import img_to_text
import cv2
from config import Start_Answer
from pprint import pprint
from parse_screen_nurseslabs import get_question_text, get_answer_text
from Tests.outs import OUT1, OUT2, OUT3
# file = Path('Tests/images/Screenshot (869).png')
# img = cv2.imread(filename=str(file))
# pprint(img_to_text(img, Start_Answer))

response = get_answer_text(OUT3[0])
print(response)