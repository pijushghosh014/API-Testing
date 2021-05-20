import requests
import json
import jsonpath

url = ('https://reqres.in/api/users')
#response = requests.post(url)
#print(response)
file = open('C:\\Users\\Pijush\\PycharmProjects\\API Testing\\New user.json','r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

response = requests.post(url,request_json)
print(response.content)

assert response.status_code == 201      #validating response code

print(response.headers)         #fatching header
print(response.headers.get('Content-Type'))
print(response.headers.get('Content-Length'))

json_response = json.loads(response.text)
id = jsonpath.jsonpath(json_response,'id')       #Fatch JsonPath of 'id'
print(id[0])