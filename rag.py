from google import genai
from dotenv import load_dotenv
import os
from google.genai import types

load_dotenv()
api_key=os.getenv("API_KEY")
client=genai.Client(api_key=api_key)
role = "You are a swimming instructor in a new school."
task = "Your job is to teach students basic swimming concepts, such as floating, breathing and kicking, in simple steps."
context = "You work at Splash Academy, a new swimming school. Your students are complete beginners, many of them children and nervous adults."
constraints = "Only answer questions about swimming."
output = "Keep answers short"

#RAG
knowledge = [
    "Beginner classes are held on Mondays and Wednesdays at 4pm.",
    "Every student must wear a swimming cap and goggles.",
    "The beginner pool is 1 metre deep.",
    "Each class lasts 45 minutes.",
]

chat = client.chats.create(
    model="gemini-3.5-flash",
    config=types.GenerateContentConfig(system_instruction=role + " " + task + constraints + " " + output + " " + context)
)

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
        
    





