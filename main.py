import os
import google.generativeai as ai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('api_key')


ai.configure(
    api_key=api_key
)

model = ai.GenertiveModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = 'In this chat, you will behave as a machine model that is specifically designed to answer questions related to health and healthcare. Any other questions are to be replied with "I am a model trained to give answers related to healthcare"'

while(True):
    question = input("You: ")

    if(question.strip()=''):
        break

    response = chat.send_message(question)
    print('\n')
    print(f"Bot: {response.text}")
    print('\n')
    instruction = ''
