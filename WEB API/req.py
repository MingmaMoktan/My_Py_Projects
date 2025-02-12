import requests

endpoint = "https://randomuser.me/api/"

response = requests.get(endpoint)
# print(response)

params = {
    "seed": "lol",
    "results": 3
}
data = response.json()
# print(data)
# print(type(data))


print(data["results"][0]["name"]["first"])