# JSON Quick Guide
## _JSON - Javascript object Notation_

## Features

- Text Format : storing and transmitting data in web applications
- JSON is language independent
- Data Representation Format
- Commonly used for APIs and Configs
- Lighweight and Easy to read/write
- Integrates easily with most languages

Types - strings , number , booleans , null , arrays [] , objects {"Key": "value"} {"age":30}

### Example
"Key": "value"/value

Key-value pairs 
JSON is a string whose format very much resembles JavaScript object literal format.
```
{
    "Key": "value",
    "key": "value"
}


{
    "Name" : "Raju",
    "age"  : 26,
    "isProgrammer" : true,
    "skills" : ["c++","python","Javascript","java"],
    "address": {
        "street" : "Gobindapur main st"
        "state"  : "Bihar"
        "Pin code": 841238
    }
}


Above it is mentioned that JSON text basically looks like a JavaScript object inside a string.
We can also convert arrays to/from JSON. Below is also valid JSON, for example:

[
  {
    "name": "Kishan",
    "age": 29,
    "skills": ["C++", "Javascript", "pHP"]
  },
  {
    "name": "Raju",
    "age": 29,
    "address": {
        "vallage":"Gobindapur"
        "city":"siwan"
        "state":"Bihar"
    }
  }
]
