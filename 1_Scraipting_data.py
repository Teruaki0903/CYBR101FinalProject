"""
* The scraping program: This program script data from website.
* Teruaki Murakami
* 2023/12/06

1. Set the URL. And get web page content.
2. get script and get data.
3. make data flame by panda.
4. Output csv file.
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def parse_strlist(sl):
    # Function to clean and parse a string list from JavaScript
    clean = re.sub("[\[\],\s]","",sl)  # Remove square brackets, commas, and whitespaces
    splitted = re.split("[\'\"]",clean)  # Split the cleaned string using single or double quotes
    values_only = [s for s in splitted if s != '']  # Remove empty strings from the list
    return values_only

# URL of the webpage containing the data
url = 'https://bitinfocharts.com/comparison/bitcoin-tweets.html#alltime'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find and extract the JavaScript data from the webpage
scripts = soup.find_all('script')
for script in scripts:
    if 'd = new Dygraph(document.getElementById("container")' in script.text:
        StrList = script.text
        StrList = '[[' + StrList.split('[[')[-1]
        StrList = StrList.split(']]')[0] +']]'
        StrList = StrList.replace("new Date(", '').replace(')','')
        dataList = parse_strlist(StrList)

# Extract date and tweet data from the parsed JavaScript data
date = []
tweet = []
for each in dataList:
    if (dataList.index(each) % 2) == 0:
        date.append(each)
    else:
        tweet.append(each)

# Create a Pandas DataFrame from the extracted data
df = pd.DataFrame(list(zip(date, tweet)), columns=["Date","Decred - Tweets"])

# Change DataFrame display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Display the DataFrame
print(df)

# Write the DataFrame to a CSV file named "output.csv"
file = open("output.csv", "w")
file.write(str(df))
