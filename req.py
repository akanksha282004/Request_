import json
import requests
re=requests.get("http://saral.navgurukul.org/api/courses")
ad=re.json()
with open("requestfile.json","w") as a:
    json.dump(ad,a,indent=4)
i=0
id=[]
while i<len(ad["availableCourses"]):
    Name=ad["availableCourses"][i]["name"]
    Id=ad["availableCourses"][i]["id"]
    id.append(Id)
    print(i," ",Name," ",Id)
    i=i+1
choose=int(input("enter the number:"))
rc=0
k=requests.get("http://saral.navgurukul.org/api/courses/"+id[choose]+"/exercises")
m=k.json()
list2=[]
for i in m["data"]:
    print(rc,i["slug"])
    list2.append(i["slug"])
    rc=rc+1
choose2=int(input("enter the slug number"))
n=requests.get("http://saral.navgurukul.org/api/courses/"+str(choose)+"exercises/getbyslug?slug="+list2[choose2])
o=n.json()
print(o)