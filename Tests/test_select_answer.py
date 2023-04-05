import unittest
from parse_screen_nurseslabs import get_nltk_index
from outs import response1, response2, response3 


class TestSelectAnswer(unittest.TestCase):
    def test_response1(self):
        self.assertEqual(get_nltk_index(response1, ['A.Chemical name ', 'B.Drugname', 'C. Generic name', 'D.Trade name']), [13, 10, 12, 11])
    
    def test_response2(self):
        self.assertEqual(get_nltk_index(response2, ['A.Chemical name ', 'B.Drugname', 'C. Generic name', 'D.Trade name']), [11, 0, 9, 6])

    def test_response3(self):
        self.assertEqual(get_nltk_index(response3, ['A.Chemical name ', 'B.Drugname', 'C. Generic name', 'D.Trade name']), [16, 9, 15, 12])
if __name__ == "__main__":
    unittest.main()