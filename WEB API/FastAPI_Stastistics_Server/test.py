import requests

# Test for the factorial
endpoint = "http://0.0.0.0:8000/api/factorial"


params = {"number": "3"}  
response = requests.post(endpoint, data=params)
data = response.json()
print(data)


# Test for the median
server = "http://0.0.0.0:8000/api/median"

params = {"numbers": ["1", "2", "3", "4", "5"]}
response = requests.post(endpoint, data=params)
data = response.json()
print(data)