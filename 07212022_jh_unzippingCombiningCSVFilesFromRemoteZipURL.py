import os
from io import BytesIO
from zipfile import ZipFile
import pandas as pd
import requests

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/IndoorMovement.zip"
content = requests.get(url)
archive = ZipFile(BytesIO(content.content))

files = [i for i in archive.namelist() if i.startswith('dataset') ]

dfList = []

for file in files:
    if file.endswith('.csv') and file != 'MovementAAL_target.csv':
            #store each csv file as dataframe
            tempdf = pd.read_csv(archive.open(file), index_col=0, header=0, delimiter=",")
            
            #Store all temp dataframes in a list object
            dfList.append(tempdf)
        

#merge the list of dataframes into a single dataframe (this assumes all dataframes have the same columns)
df = pd.concat(dfList)
print(df.head(25))

archive.close()

cwd = os.getcwd()
path = cwd

df.to_csv("testing2.csv", sep=',', encoding='utf-8')

# *****************************************************************#
# everything below this line is experimental

'''
for datadirectory in archive.namelist():
    if datadirectory.startswith('dataset/'):
        archive.extract(datadirectory)
'''

'''
    if datadirectory.startswith('dataset/'):
        for sheet in archive.namelist():
            tempdf = pd.read_csv(sheet, index_col=0, header=0)
            data.append(tempdf)
'''

#df = pd.concat(data, axis=1)

#print(df)


'''

dfs += [pd.read_csv(zf.open('*.csv')]

dfs = []

s_dir = lambda zipinfo: zipinfo.filename.endswith('/')

with zf as z:    
    for filename in z.namelist():
        file_info = z.getinfo(filename)
        if file_info.is_dir():
            # read the file
            if filename.endswith('.csv'):
                for line in z.open(filename):
                    #df = pd.read_csv(zf.open(line))
                    #print(line.decode('utf-8'))
                    
                    #zip_file = os.path.join(zf, filename)
                    #zf = zipfile.ZipFile(zip_file)
                    dfs += [pd.read_csv(z.open(filename), header=None, sep=";", encoding='latin1') for f in z.namelist()]

df = pd.concat(dfs,ignore_index=True)
'''