from parse_screen_nurseslabs import get_question_text, get_answer_text, get_nltk_index
from Tests.outs import OUT1, OUT2, OUT3, response1, OUT6, response4, response5, response6, response7, response2, response3, response8, response9, response10, response11
from pathlib import Path
import cv2
from img_to_text import img_to_text
from config import Start_Answer, chars_answer, symbols_answer
from pprint import pprint


# file = Path('Tests/images/multichoise.png')
# img = cv2.imread(filename=str(file))
# OUT = img_to_text(img, chars_answer, symbols_answer)

# get_question_text = get_question_text(OUT[0])
# get_answer_text = get_answer_text(OUT[0])

# print(get_question_text)
# print(get_answer_text)
response = get_nltk_index(response11, ['A.Record the number of stools per day.', 'B. Maintain strict intake and output records.', 'C.Sterile technique for dressing change at IV site.', 'D. Monitor for cardiac arrhythmias.'])
print(response)
# response = get_answer_text(OUT3[0])
# print(response)