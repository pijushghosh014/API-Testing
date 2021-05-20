import requests
#import json
#import jsonpath

url = "https://reqres.in/api/users/2"
response = requests.delete(url)
print(response)