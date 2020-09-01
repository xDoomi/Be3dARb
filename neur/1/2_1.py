import re

inFile = open('neur/1/sentences.txt')
outFile = open('neur/1/outFile.txt', 'w')
spisok = []
for line in inFile:
    stroka = re.split('[^a-z]', line.lower())
    spisok.append(stroka)
index = 0
for i in range(len(spisok)):
    for j in range(len(spisok[i])):
        if spisok[i][j] == '':
            index += 1
for i in range(index):
    spisok.remove("")
print(spisok, file = outFile)