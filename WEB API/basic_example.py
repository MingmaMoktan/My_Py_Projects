import requests
import json

key = ""
max_completion_tokens = 50
temperature = 1
old_responses = []

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
    
    old_responses.append({
      "role": "user",
      "content": prompt
    })

    r = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))
    r_json = r.json()
    old_responses.append(r_json["choices"][0]["message"])
    # print(r_json)
    print("\n")
    print(old_responses[0]['content'])
    print("\n")
    print(r_json["choices"][0]["message"]["content"])
    return prompt

while True:
    prompt = input("Enter the prompt here: ")
    if prompt.lower() == "exit":
        break
    else:
        response = chatgpt_query(prompt)
        # print(response)
