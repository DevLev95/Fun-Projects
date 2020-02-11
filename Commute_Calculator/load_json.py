#success
import json

#read file
with open('7.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

# turned the json into a list that i can actually use
# obj is a list in a dict in a list
a = obj[0]
b = a["cities"]
