"""
Here to use this chatbot application you can use the openAI Key by purchasing.
You should also install the openAi by using the following command.4
- pip install openai

And you can also see the documentation how to use the openai
Here is the url for the documentation.
url = https://platform.openai.com/docs/overview

You can go the url = https://platform.openai.com/settings/organization/api-keys

And there you can purchase the key in minimal price and then use this chatbot application.
"""

import os
from openai import OpenAI

key = os.getenv("OPENAI_API_KEY")
if not key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=key)

messages = []

def completion(message):
    global messages
    messages.append({
        "role": "user",
        "content": message
    })
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o"
    )
    assistant_message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(assistant_message)
    print(f"Assistant: {assistant_message['content']}")

if __name__ == "__main__":
    print("Assistant: Hi, I am assistant. How may I help you?\n")
    while True:
        user_question = input()
        if user_question.lower() == "quit":
            print("Thank you. If you need help again, you can come back.")
            break
        completion(user_question)
