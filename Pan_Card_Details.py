import http.client
import json
from prettytable import PrettyTable
mypan=input('enter your pan card=')
conn = http.client.HTTPSConnection("pan-card-verification1.p.rapidapi.com")

payload = "{\n    \"task_id\": \"74f4c926-250c-43ca-9c53-453e87ceacd1\",\n    \"group_id\": \"8e16424a-58fc-4ba4-ab20-5bc8e7c3c41e\",\n    \"data\": {\n        \"id_number\": \""+mypan+"\"\n    }\n}"

headers = {
    'content-type': "application/json",
    'X-RapidAPI-Key': "xxxxxxxxxxxxxxxxxxxx",
    'X-RapidAPI-Host': "pan-card-verification1.p.rapidapi.com"
    }

conn.request("POST", "/v3/tasks/sync/verify_with_source/ind_pan", payload, headers)

res = conn.getresponse()
data = res.read()

mydata=json.loads(data.decode("utf-8"))
check=mydata['status']
if check=='completed':
    adhar=mydata['result']['source_output']['aadhaar_seeding_status']
    fname=mydata['result']['source_output']['first_name']
    lname=mydata['result']['source_output']['last_name']
    noc=mydata['result']['source_output']['name_on_card']

    head=['aadhaar_seeding_status','First_name','Last_name','name_on_card']
    myheading=PrettyTable(head)
    data=[adhar,fname,lname,noc]
    myheading.add_row(data)
    print(myheading)
else:
    print('invalid pan card')
