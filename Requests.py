import requests
import json

url=requests.get("https://api.merakilearn.org/courses")
data=url.json()
with open("courses1.json","w") as file:
    json.dump(data,file,indent=4)
i=0
while i<len(data):
    print(i+1,")",data[i]["name"],":",data[i]["id"])
    i=i+1
user=int(input("enter which programme do you want:"))
print(data[user-1]["name"],":",data[user-1]["id"])
content_file=data[user-1]["name"]+"_"+data[user-1]["id"]
link="http://api.merakilearn.org/courses/"+data[user-1]["id"]+"/exercises"
url1=requests.get(link)
data1=url1.json()
with open(content_file,"w") as file1:
    json.dump(data1,file1,indent=4)

i=0
while i<len(data1["course"]["exercises"]):
    print(i+1,")",data1["course"]["exercises"][i]["name"])
    i=i+1

topic=int(input("Enter topic number whichever you want:"))
topic_index=topic-1
i=0
while i<len(data1["course"]["exercises"][topic_index]["content"]):
    print(data1["course"]["exercises"][topic_index]["content"][i]["value"])
    i=i+1

while topic_index<=len(data1["course"]["exercises"]):
    next_privious=input("Enter Next or Privious n/p :")
    if next_privious=="p":
        topic_index=topic_index-1
        if 1<=topic_index:
            print(data1["course"]["exercises"][topic_index]["name"])
            i=0
            while i<len(data1["course"]["exercises"][topic_index]["content"]):
                print(data1["course"]["exercises"][topic_index]["content"][i]["value"])
                i=i+1
        elif topic_index==0:
            print(data1["course"]["exercises"][topic_index]["name"])
            i=0
            while i<len(data1["course"]["exercises"][topic_index]["content"]):
                print(data1["course"]["exercises"][topic_index]["content"][i]["value"])
                i=i+1
        else:
            print("finished")
            break
    elif next_privious=="n":
        topic_index=topic_index+1
        if topic_index<len(data1["course"]["exercises"]):
            print(data1["course"]["exercises"][topic_index]["name"])
            i=0
            while i<len(data1["course"]["exercises"][topic_index]["content"]):
                print(data1["course"]["exercises"][topic_index]["content"][i]["value"])
                i=i+1
        if topic_index==len(data1["course"]["exercises"]):
            print("Topic is completed")
            break
    else:
        print("user input is wrong:")
        break
