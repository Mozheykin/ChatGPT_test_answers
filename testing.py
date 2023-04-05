from parse_screen_nurseslabs import get_question_text, get_answer_text, get_nltk_index
from Tests.outs import OUT1, OUT2, OUT3, response1
# file = Path('Tests/images/Screenshot (869).png')
# img = cv2.imread(filename=str(file))
# pprint(img_to_text(img, Start_Answer))

response = get_nltk_index(response1, ['A.Chemical name ', 'B.Drugname', 'C. Generic name', 'D.Trade name'])
response = get_answer_text(OUT3[0])
print(response)