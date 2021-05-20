import requests
import json
import jsonpath
url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
print(response)                 #Pick Response
print(response.content)         #Display Response
print(response.headers)