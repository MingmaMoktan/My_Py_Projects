import requests
import json
# Testing the start_session
endpoint = "http://0.0.0.0:8000/api/start_session/"
params = {"username": "David"}
response = requests.get(endpoint, params=params)
data = response.json()
print(data)