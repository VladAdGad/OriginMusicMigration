import json
import re

with open('Resources/config.json') as json_data_file:
    data = json.load(json_data_file)
    path = data['path']
    outPutFile = data['outPutFile']

dictionary = {}

for line in open(outPutFile):
    link = re.search('^https://www.deezer.com/track/\w+', line).group()
    name = re.search('\s+.*', line).group()
    dictionary[link] = name[1:]

with open(outPutFile, "w") as myFile:
    for k, v in dictionary.items():
        myFile.write(k + '\t' + v + '\n')


