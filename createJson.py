import json

myDict = {
    "Users" : [
        {
            "id" :1,
            "name":"suraj",
            "city":"patna"
        },
        {
            "id" :2,
            "name":"Niraj",
            "city":"Ranchi"
        },
        {
            "id" :3,
            "name":"Monu",
            "city":"Siwan"
        },
        {
            "id" :4,
            "name":"Kishan",
            "city":"Prayagraj"
        },        
        {
            "id" :5,
            "name":"Shivam",
            "city":"Banaras"
        },      

    ]
}

# load & dumps
# create JSON file by using dumps

json_string = json.dumps(myDict , indent=4)

with open('jsonData.json','w') as f:
    f.write(json_string)

