

url = " © https://nurseslabs.com/nursing-pharmacology-nclex-practice-questions-test-bank/"


def get_question(data:dict, split_chars:list=[':','©','()','\{\}']) -> str:
    question = dict()
    for index, dict_t in enumerate(data):
        splits = [split_char in dict_t.get('text') for split_char in split_chars]
        if 'Question' in dict_t.get('text'):
            question['start_index'] = index + 1
            print(f'[START INDEX] {index}, word: {dict_t.get("text")}')
        elif all([any(splits), question.get('start_index') is not None]):
            question['end_index'] = index
            print(f'[END INDEX] {index}, word: {dict_t.get("text")}')
        else:
            start = question.get('start_index')
            end = question.get('end_index')
            if all([
                start is not None,
                end is not None]):
                return ' '.join([word.get('text').strip() for word in data[start: end]])
        



def get_answer():
    ...

