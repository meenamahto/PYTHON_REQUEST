import requests
import json
import os

x = requests.get('https://api.merakilearn.org/courses')
p=x.json()
file=os.path.exists("course.json")
if file==True:
    serial_number=1
    with open("course.json","r") as f:
        a=json.load(f)
    for i in a:
        print(serial_number,i["name"],":",i["id"])
        serial_number+=1
else:
    print("file is not exists")
