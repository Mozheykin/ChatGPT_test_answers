import openai
from config import model, max_tokens, temperature, top_p, frequency_penalty, API_KEY


def get_response(request:str) -> dict:
#     prompt = f"""I will give you a multiple choice question with answers indicated by 0,1,2,3.
# Please tell me the number of the option that best answers the question.
# Only provide a single number without any additional explanation or text.
# Choose one of the options 0, 1, 2, or 3. 
# {request}"""

    prompt = f"""I will give you a multiple choice question, the answers are labeled A, B, C, D.
Send me back the complete correct answer. Without any additional characters and words. {request}"""


    messages = [
        {
            'role': 'system',
            'content': 'Help answering questions.'
        },
        {
            'role': 'user',
            'content': prompt
        }
    ]

    openai.api_key = API_KEY
    return openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
    )


def get_answer(response:dict) -> str:
    return response['choices'][0]['message']['content'].strip()