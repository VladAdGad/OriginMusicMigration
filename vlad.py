import os
import re
import json
import urllib.request
import urllib.parse

path = 'E:/Cloud/Vlad/Multimedia/Music'

for file in os.listdir(path):
    fileName = os.path.splitext(file)[0]

    fileName = str(fileName)
    fileName = re.sub('[^A-Za-z0-9 ]', '', fileName)
    for i in range(10):
        fileName = re.sub('  ', ' ', fileName)
    fileName = re.sub(' ', '%20', fileName)

    print(fileName)

    urllib.parse.quote_plus(fileName)
    dataOfTrack = urllib.request.urlopen("https://api.deezer.com/search?strict=on&q=" + fileName)

    contents = json.load(dataOfTrack)
    data = contents.get('data', None)

    with open("downloadLinks.txt", "a") as myFile:
        for song in data:
            line = (song['link'] + '\t' + str(song['title'].encode("utf-8")))
            print(line)
            myFile.write(line + '\n')
    # else:
    #     print('Deezer has no songs for this query')
