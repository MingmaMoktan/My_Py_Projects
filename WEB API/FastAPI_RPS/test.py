import requests
import json
# Testing the start_session
endpoint = "http://0.0.0.0:8000/api/start_session/"
response = requests.get(endpoint)
data = response.json()
print(json.dumps(data, indent=4))


# Testing the join session
# Player 1
session_id = data.get("session_id")
endpoint = "http://0.0.0.0:8000/api/join_session/"
params = {"session_id": session_id, "username": "David", "choice": "scissors"}
response = requests.get(endpoint, params=params)
data = response.json()
print(json.dumps(data, indent=4))

# Player 2
params = {"session_id": session_id, "username": "Salome", "choice": "paper"}
response = requests.get(endpoint, params=params)
data = response.json()
print(json.dumps(data, indent=4))

# Testing the info_session
endpoint = "http://0.0.0.0:8000/api/session_info/"
params = {"session_id": session_id}
response = requests.get(endpoint, params=params)
data = response.json()
print(json.dumps(data, indent=4))