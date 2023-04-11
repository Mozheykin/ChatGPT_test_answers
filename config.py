import env

# ChatGPT Settings:

API_KEY = env.API_KEY
model="gpt-3.5-turbo" 
temperature=0.7 
max_tokens=256
top_p=1.0
frequency_penalty=0
presence_penalty=0


# Select question
Start_Question = ['Question',]
End_Question = [':','©','()','\{\}']

# Select answers
# Start_Answer = ['©','()','\{\}', '@', 'A.', 'B.', 'C.', 'D.', 'F.', 'E.', ]# or insert list symbols [':','©','()','\{\}']
chars_answer = [r'A\.', r'B\.', r'C\.', r'D\.', r'F\.', r'E\.',]
symbols_answer = ['©','()','\{\}', '@',]
Start_Answer = [*chars_answer, *symbols_answer]
End_Answer = Start_Answer.copy() 
End_Answer.append('.')