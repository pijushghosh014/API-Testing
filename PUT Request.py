import requests
import json
import jsonpath

url = ('https://reqres.in/api/users/2')
#response = requests.put(url)
#print(response)

file = open('C:\\Users\\Pijush\\PycharmProjects\\API Testing\\New user.json','r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

response = requests.put(url,request_json)
print(response.content)

assert response.status_code == 200      #validating response code

json_response = json.loads(response.text)
updatedAt = jsonpath.jsonpath(json_response,'updatedAt')       #Fatch JsonPath of 'updated at'
print(updatedAt[0])