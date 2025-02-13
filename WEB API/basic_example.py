import requests
import json

key = "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"
max_completion_tokens = 50
temperature = 1

def chatgpt_query(prompt):
    headers = {
        "Authorization": "Bearer " + key,
        "Content-Type": "application/json"
    }
    data = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_completion_tokens": max_completion_tokens,
        "temperature": temperature,
        "model": "gpt-4o"
    }

    r = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))
    r_json = r.json()
    print(r_json)
    print("\n")

    print(r_json["choices"][0]["message"]["content"])
    return prompt

while True:
    prompt = input("Enter the prompt here: ")
    if prompt.lower() == "exit":
        break
    else:
        response = chatgpt_query(prompt)
        print(response)
