from google import genai
from dotenv import load_dotenv
import os
from google.genai import types

load_dotenv()
api_key=os.getenv("API_KEY")
client=genai.Client(api_key=api_key)
chat=client.chats.create(model="gemini-3.5-flash")

print ("Started")

while True:
    message=input("you: ")
    
    if message.lower() == "exit":
        print("Goodbye!")
        break
    
    try:
        response = chat.send_message(message)
        print("Gemini: ", response.text)
        
    except Exception as error:
        print("error: ", error)
        
    





