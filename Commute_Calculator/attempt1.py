from selenium.webdriver import Chrome
import pandas as pd
import json
import itertools

# read file
with open('7.json', 'r') as myfile:
    data=myfile.read()
# parse file
obj = json.loads(data)

# turned the json into a list that i can actually use
# obj is a list in a dict in a list
a = obj[0]
cities = a["cities"]

#panda experiment
total = []

for city in cities:
#for city in itertools.islice(cities,0,2):

    print(city)

    #Avalon + ",+Los+Angeles,+CA/"
    #"Northridge,+Los+Angeles,+CA/"

    city_URL = city+",+Los+Angeles,+CA/"
    # JESUS CHRIST make sure to include /chromedriver after temporary_paath
    webdriver = "/Users/levon/Documents/coding/temporary_paath/chromedriver"

    driver = Chrome(webdriver)
    
    URL = "https://www.google.com/maps/dir/Westaire+Engineering+Inc,+5820+Alameda+St,+Vernon,+CA+90058/"+city_URL
    driver.get(URL)

    hovik_commute = driver.find_element_by_class_name("section-directions-trip-numbers").text
    new = ((city+" commute Hovik",hovik_commute))
    total.append(new)
