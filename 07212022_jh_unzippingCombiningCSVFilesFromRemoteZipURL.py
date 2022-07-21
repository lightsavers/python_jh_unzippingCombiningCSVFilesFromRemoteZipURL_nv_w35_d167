''' **********************
*
* Author: lightsavers
* Created: 07212022
*
***********************'''

import os
from io import BytesIO
from zipfile import ZipFile
import pandas as pd
import requests

# Sample remote URL ZIp file
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/IndoorMovement.zip"

#store URL connection in variable to extract contents next
content = requests.get(url)

#use zipfile and BYtesIO to store contents in zipfile object
archive = ZipFile(BytesIO(content.content))

#iterate thru files inside zip and identify folder 'dataset'
files = [i for i in archive.namelist() if i.startswith('dataset') ]

# declare empty list to store future dataframes
dfList = []

# iterate thru the files inside the 'dataset' directory and append them to list
for file in files:
    if file.endswith('.csv') and file != 'MovementAAL_target.csv':
            #store each csv file as dataframe
            tempdf = pd.read_csv(archive.open(file), index_col=0, header=0, delimiter=",")
            
            #Store all temp dataframes in a list object
            dfList.append(tempdf)
        

#merge the list of dataframes into a single dataframe (this assumes all dataframes have the same columns)
df = pd.concat(dfList)

#print top 25 rows to console or terminal
print(df.head(25))

#close archive object connection
archive.close()

#list current working directory
cwd = os.getcwd()

#store path of current working directory in variable
path = cwd

#save file dataframe to csv file
df.to_csv("testing2.csv", sep=',', encoding='utf-8')
