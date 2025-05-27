import os
from openai import OpenAI

key="Type your own sk key"

messages=[]

client = OpenAI(
    api_key=key,
)

def completion(message):
    global messages

   
    messages.append(
                {
                    "role":"user",
                    "content":message,
                }
            )
    
    chat_completion = client.chat.completions.create( messages=messages,model="gpt-4o")

        

    print(chat_completion)

    message = {
        "role": "assistant",
        "content" : chat_completion.choices[0].message.content
    }
    messages.append(message)

    print(f"Jarvis: {message["content"]}")


if __name__ == "__main__":
    user_question = input("Hi i am Jarvis,How may i help you\n")
    while True:

        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)


