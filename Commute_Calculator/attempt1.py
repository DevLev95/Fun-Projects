from selenium.webdriver import Chrome
import pandas as pd
import json
import itertools

# read file
with open('7.json', 'r') as myfile:
    data=myfile.read()
# parse file
obj = json.loads(data)
