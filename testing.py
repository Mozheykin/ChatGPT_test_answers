from parse_screen_nurseslabs import get_question_text, get_answer_text, get_nltk_index
from Tests.outs import OUT1, OUT2, OUT3, response1, OUT6, response4, response5, response6, response7, response2, response3, response8, response9, response10, response11, response12
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
# response = get_nltk_index(response12, ['A. “It will slow down the replication of the virus.”', 'B. “This medication will improve your child’s overall health status.”', 'C.“This medication is used to prevent bacterial infections.”', 'D. “It will increase the effectiveness of the other medications your child receives.”'])
# print(response)
# response = get_answer_text(OUT3[0])
# print(response)

# string = ' A. The client must take the medication at evenly spaced intervals. OB. The client may save leftover medication For a Future illness. OQ C.IFsigns of an allergic reaction, continue the medication and notify the physician. OD. Clients taking oral contraceptives must be cautioned to use an alternate Form of birth control while being treated with penicillin.'

# import re 

# result = [answer.strip() for answer in re.split(r'(?:\s|O|^)[A-Z]\.', string=string) if answer.strip() != '' ]

# # result = [answer.strip() for answer in re.split(r'(?:O?[A-Z]\.)(?:\s)(.*?)(?:O?[A-Z]\.|$)', string=string)[1:] if answer]

print(result)