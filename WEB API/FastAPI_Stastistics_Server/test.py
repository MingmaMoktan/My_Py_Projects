import requests
import json

# Test for the factorial
endpoint = "http://0.0.0.0:8000/api/factorial/"


params = {"number": 3}  
response = requests.post(endpoint, data=params)
data = response.json()
print(data)


# Test for the median
endpoint = "http://0.0.0.0:8000/api/median/"

params = {"numbers": json.dumps([1,2,3,4,5,6])}
response = requests.post(endpoint, data=params)
data = response.json()
print(data)


# Test for the variance
endpoint = "http://0.0.0.0:8000/api/variance/"

params = {"numbers": json.dumps([1,2,3,4,5,6])}
response = requests.post(endpoint, data=params)
data = response.json()
print(data)


# Test for the pstdev
endpoint = "http://0.0.0.0:8000/api/pstdev/"

params = {"numbers": json.dumps([1,2,3,4,5,6])}
response = requests.post(endpoint, data=params)
data = response.json()
print(data)