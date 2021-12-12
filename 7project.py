person={}
person["john"]={
    "name":"John Smith","ID":1000,"Gender":"f",
    "DOB":"01/01/2000","zipcode":"08122-2324",
    "age":20,"Amount":"1500.20"
    }
person["jim"]={
    "name":"Jim McDonald","ID":2000,"Gender":"m",
    "DOB":"02/02/2020","zipcode":"08136-2324",
    "age":25,"Amount":"1500.20"
    }
person["jim"]={
    "name":"Jim McDonald","ID":20,"Gender":"m",
    "age":20,"Amount":"1500.20"
    }
print("person")
print(type(person))

import json
a=json.dumps(person)
print(a)
print(type(a))

import json
with open('texty.txt') as f:
    lines = f.readlines()
    print(lines)
