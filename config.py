import os
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
Start_Answer = ['©','()','\{\}', '@']# or insert list symbols [':','©','()','\{\}']
End_Answer = Start_Answer.copy() 
End_Answer.append('.')