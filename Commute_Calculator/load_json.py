#success
import json

#read file
with open('7.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)
