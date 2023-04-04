import unittest
from parse_screen_nurseslabs import get_answers, get_question, get_question_text, get_answer_text
from config import Start_Answer
from outs import OUT1, OUT2, OUT3, OUT4, OUT5


class TestParse(unittest.TestCase):
    def test_question(self):
        self.assertEqual(get_question_text(OUT1[0])[0], 'Ss ')
    
    def test_question1(self):
        self.assertEqual(get_question_text(OUT2[0])[0], 'The interaction of one drug increased by the presence of a second drug is known as: ')

    def test_answer(self):
        self.assertEqual(get_answer_text(OUT1[0]), ['A.Chemical name ', ' B.Drugname ', 'C. Generic name ', ' D.Trade name'])

    def test_answer1(self):
        self.assertEqual(get_answer_text(OUT2[0]), ['A. Potentiation ', ' B. Addictive effects ', 'C.Antagonism ', ' D.Synergism'])

    def test_answer2(self):
        self.assertEqual(get_answer_text(OUT3[0]), ['Temperature 99.9° F (37.7° C) ', ' Blood pressure 196/100 ', 'Apical pulse rate 86 beats/minute ', ' Respiratory rate 16 per minute « Previous Next >'])

if __name__ == "__main__":
    unittest.main()