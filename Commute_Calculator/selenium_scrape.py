from selenium.webdriver import Chrome
import pandas as pd

# JESUS CHRIST make sure to include /chromedriver after temporary_paath
webdriver = "/Users/levon/Documents/coding/temporary_paath/chromedriver"
driver = Chrome(webdriver)

URL = "https://www.google.com/maps/dir/Westaire+Engineering+Inc,+5820+Alameda+St,+Vernon,+CA+90058/Northridge,+Los+Angeles,+CA/"
driver.get(URL)
test = driver.find_element_by_class_name("section-directions-trip-numbers").text
print(test)
