import nltk
import re

url = " © https://nurseslabs.com/nursing-pharmacology-nclex-practice-questions-test-bank/"


def get_question(data:dict, start_questions:list=['Question'], split_chars:list=[':','©','()','\{\}']) -> str:
    question = dict()
    for index, dict_t in enumerate(data):
        splits = [split_char in dict_t.get('text') for split_char in split_chars]
        start_question = [questions in dict_t.get('text') for questions in start_questions]
        if any(start_question): 
            question['start_index'] = index + 1
            print(f'[START INDEX] {index}, word: {dict_t.get("text")}')
        elif all([any(splits), question.get('start_index') is not None]):
            question['end_index'] = index + 1
            print(f'[END INDEX] {index}, word: {dict_t.get("text")}')
        else:
            start = question.get('start_index')
            end = question.get('end_index')
            if all([
                start is not None,
                end is not None]):
                return ' '.join([word.get('text').strip() for word in data[start: end]])
        


def get_question_text(data:dict) -> str:
    text = ' '.join(dict_t.get('text') for dict_t in data)
    question = re.search(r'(?:\d\.\s[Qq]uestion\s)(.*?\s)(?:@|©)', text)
    if not question:
        question = re.search(r'(?:\s[Qq]uestion\s\d*\s\d\s\w*\s)(.*?\s)(?:@|©)', text)
        if question:
            return question[1].strip()
    else:
        return question[1].strip()


def get_answer_text(data:dict) -> list:
    text = ' '.join(dict_t.get('text') for dict_t in data).strip()
    # print(text)
    answers = re.search(r'(@|©)(\s\w\.)(.*)$', text)
    # print(answers)
    if answers is None:
        answers = re.search(r'(\sA\.)(\s\w)(.*)$', text)
    if answers is None:
        answers = re.search(r'(@|©)(\s\w)(.*)$', text)
    if answers is not None:
        result = [answer.strip() for answer in re.split(r'(?:@|©)(?:\s)(.*?)(?:@|©|$)', answers[0]) if answer]
        if len(result) < 2:
            result = [answer.strip() for answer in re.split(r'(?:[A-Z]\.)(?:\s)(.*?)(?:[A-Z]\.|$)', answers[0])[1:] if answer]
        return result
    else:
        return []
    


def get_answers(data:dict, char_split:str='©'):
    text = ' '.join([text.get('text') for text in data])
    result = text.split(char_split)
    return result[1:] 


def get_parse_answer(answer_gpt:str) -> list:
    answer = re.search(r'(?:Answer:\s)(.*$)', answer_gpt)
    if answer:
        # answers = [x.group() for x in re.finditer(r'[A-Z](\.|\))(.*?)(?:[A-Z]\.|$)', answer[1])]
        answers = re.split(r'[A-Z][\.\)]', answer[1])
        answers = [answer.strip() for answer in answers if answer]
        if answers:
            return answers
        answers = answer[1]
        if answers:
            return answers
        print(answers)
    else:
        return [answer_gpt]

def get_nltk_index(answer_gpt:str, answers:list) -> list:
    result = list()
    list_answers = get_parse_answer(answer_gpt=answer_gpt)
    for res in list_answers:
        result_list = list()
        for answer in answers:
            result_list.append(nltk.edit_distance(answer, res))
        min_index = result_list.index(min(result_list))
        result.append([1 if index == min_index else 0 for index in range(len(result_list))])
    return result