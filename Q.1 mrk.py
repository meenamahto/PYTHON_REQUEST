import requests
import json
import pprint

url='https://api.merakilearn.org/courses'
response=requests.get(url)
print(response.status_code)

data=response.json()
if response.status_code==200:
    d=json.loads(response.text)
    pprint.pprint(d)
    print(type(d))
else:
    print("not")
with open("course.json","w") as file:
    json.dump(data,file,indent=4)

