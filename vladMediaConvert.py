import os
import re
import json
import urllib.request
import urllib.parse


def make_file_empty(out_put_file):
    open(out_put_file, "w").close()


def leave_one_space(file_name):
    for i in range(10):
        file_name = re.sub(r'\s+', ' ', file_name)
        return file_name


def space_to_html_representation(file_name):
    file_name = re.sub(' ', '%20', file_name)
    return file_name


def lead_to_html_representation(file_name):
    file_name = leave_one_space(file_name)
    file_name = re.sub('[^A-Za-z0-9 ]', '', file_name)
    file_name = space_to_html_representation(file_name)
    return file_name


with open('Resources/config.json') as json_data_file:
    data = json.load(json_data_file)
    path = data['path']
    outPutFile = data['outPutFile']

make_file_empty(outPutFile)

for file in os.listdir(path):
    fileName = os.path.splitext(file)[0]

    fileName = lead_to_html_representation(fileName)
    print("File Name: " + fileName)

    try:
        dataOfTrack = urllib.request.urlopen("https://api.deezer.com/search?strict=on&q=" + fileName)
    except TimeoutError:
        continue

    contents = json.load(dataOfTrack)

    if 'data' in contents and len(contents['data']) > 1:
        data = contents['data'][0]
        with open("downloadLinks.txt", "a") as myFile:
            line = (data['link'] + '\t' + str(data['title'].encode('utf-8'))[1:])
            print(line)
            myFile.write(line + '\n')
