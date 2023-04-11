from parse_screen_nurseslabs import get_question_text, get_answer_text, get_nltk_index
from Tests.outs import OUT1, OUT2, OUT3, response1, OUT6
from pathlib import Path
import cv2
from img_to_text import img_to_text
from config import Start_Answer, chars_answer, symbols_answer
from pprint import pprint


file = Path('Tests/images/Screenshot from 2023-04-02 22-35-47.png')
img = cv2.imread(filename=str(file))
pprint(img_to_text(img, chars_answer, symbols_answer))

# response = get_nltk_index(response1, ['A.Chemical name ', 'B.Drugname', 'C. Generic name', 'D.Trade name'])
# response = get_answer_text(OUT6[0])
# print(response)