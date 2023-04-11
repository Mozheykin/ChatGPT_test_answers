import unittest
from parse_screen_nurseslabs import get_nltk_index
from outs import response1, response2, response3 


class TestSelectAnswer(unittest.TestCase):
    def test_response1(self):
        self.assertEqual(get_nltk_index(response1, ['A.Chemical name ', 'B.Drugname', 'C. Generic name', 'D.Trade name']), [[0, 1, 0, 0]])
    
    def test_response2(self):
        self.assertEqual(get_nltk_index(response2, ['A.Chemical name ', 'B.Drugname', 'C. Generic name', 'D.Trade name']), [[0, 1, 0, 0]])

    def test_response3(self):
        self.assertEqual(get_nltk_index(response3, ['A.Chemical name ', 'B.Drugname', 'C. Generic name', 'D.Trade name']), [[0, 1, 0, 0]])
    
    # def test_response_chatgpt_1(self):
    #     self.assertEqual(parse_answer, 'Answer: A) Partial thromboplastin time. B) Prothrombin time.')

    
if __name__ == "__main__":
    unittest.main()