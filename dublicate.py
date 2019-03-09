import re

file = open("C:/Projects/MusicOrigin/downloadLinks.txt")

sett = set()

# for line in file:
#     title = re.sub('^[^ ]+\t', '', line)
#     print("AFTER " + title)
#     sett.add(title)

for line in file:
    lineTab = line.split('\t')
    print(lineTab)



