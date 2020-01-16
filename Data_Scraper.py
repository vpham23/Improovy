import os
import sys
import csv
import json
import re
from selenium.webdriver import Chrome
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from googlesearch import search

os.environ["PATH"] += os.pathsep + r'C:\Windows'

# sets driver to Google Chrome Driver
driver = webdriver.Chrome()

query = input("Enter the address: ")
for i in search(query, tld='com', num = 10, stop = 1, pause = 2):
    print(i)
    driver.get(i)

#driver.get("https://www.redfin.com/IL/Chicago/924-W-Fullerton-Ave-60614/unit-3/home/13359650")

# sets variable content to driver 
content = driver.page_source

# sets variable soup to data found from scraping w/ BeautifulSoup
html_soup = BeautifulSoup(content, 'html.parser')
total_Items = []

type(html_soup)
house_containers = html_soup.find_all('span', class_ = 'entryItemContent')
house_information = html_soup.find_all('h3', class_ = 'title font-color-gray-dark font-weight-bold propertyDetailsHeader')
house_bigContainers = html_soup.find_all('div', class_ = 'super-group-title')
house_groupBlock = html_soup.find_all('div', class_ = 'amenity-group')

house_superTitles  = []
house_headers = []
house_content = []
house_group = []

for div in house_bigContainers:
    house_superTitles.append(div.getText().split('\n')[0])
#print(house_superTitles)

for h3 in house_information:
    house_headers.append(h3.getText().split('\n')[0])
#print(house_headers)

# ALL HOUSE CONTENT
for span in house_containers:
    house_content.append(span.getText().split('\n')[0])
#print(house_content)

for div in house_groupBlock:
    house_group.append(div.getText().split('\n')[0])
#print(house_group)

contentFound = []

#toFind = input("Enter what you want to find: ")             # has user input what they want to find
#for num, header in zip(house_headers, house_group):         # iterates through headers
#    #print(num)
#    if num == toFind:                                       # if what the user input is the title of the header
#       print(header)                                        # prints respective block of information
#       contentFound.append(header)
     
#check if listing does not have x    
 
substring = 'Size:'
print("The following rooms have been found with that info: ")

for num in house_group:
    if num.find(substring) != -1:
       num = re.sub('([A-W])', r' \1', num)
       print(num)
       contentFound.append(num)
        
print(" ")

# 11/14 
# Have user input for address
# Then print "Following rooms have been found with that info: Master Bedroom: Dimension, etc." 
# Then send to file/web-based file
    # Format of displaying information
     
# df.to_csv('Houses.csv')
# print(df.info())
# driver.close()

# save as json object for easier parsing (another fxn)
# application for zillow --> crosscheck?

def writeToJson(path, filename, data):
    filePathName = './' + path + '/' + fileName + '.json'
    with open(filePathName, 'w') as write_file:
        json.dump(data, write_file, indent=4)

path = './'
fileName = 'House_Information'
house_content = ', '.join(house_content)
data = {"House Information": house_content}
writeToJson(path, fileName, data)

fileName = 'Data_Found'
house_content = ', '.join(contentFound)
data = {"Content Found": contentFound}
writeToJson(path, fileName, data)

#bonus:  
    #pull photo with  alt/title tags (address)
        #title tag gives number of photos

# 11/21
# Gravity Forms docs 
    # developer documentation 
    # Determine hook to feed info into function
    # wordpress docs

# 11/24
# Hook and gravity form
# See if need to run python script on another machine

# 12/15
# create address field and from address field be able to run script
    # want to be able to determine sq. footage w/o asking

