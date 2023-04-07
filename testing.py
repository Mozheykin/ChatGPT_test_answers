from parse_screen_nurseslabs import get_question_text, get_answer_text, get_nltk_index
from Tests.outs import OUT1, OUT2, OUT3, response1
from pathlib import Path
import cv2
from img_to_text import img_to_text
from config import Start_Answer
from pprint import pprint
from parse_screen_nurseslabs import get_question_text


file = Path('Tests/images/Screenshot (864).png')
img = cv2.imread(filename=str(file))
out = img_to_text(img, Start_Answer)
question = get_question_text(out[0])
print(question)




# response = get_nltk_index(response1, ['A.Chemical name ', 'B.Drugname', 'C. Generic name', 'D.Trade name'])
# response = get_answer_text(OUT3[0])
# print(response)