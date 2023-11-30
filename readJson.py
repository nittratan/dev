import json

with open('jsonData.json','r') as f:
    json_object = json.loads(f.read()) # creating object of JSON data
    f.read()

print(json_object)
print("\n")

print(json_object.items())

print("\n")

print(json_object['Users'][0])
print(json_object['Users'][1]['name'])
print(json_object['Users'][2]['city'])