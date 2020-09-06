import re
import numpy as np
import scipy.spatial

inFile = open('neur/1/sentences.txt')
outFile = open('neur/1/outFile.txt', 'w')
spisok = []
myDict = {}
for line in inFile:
    stroka = re.split('[^a-z]', line.lower())
    while '' in stroka:
        stroka.remove('')
    spisok.append(stroka)
index = 0
for i in spisok:
    for j in i:
        if not j in myDict:
            myDict[j] = index
            index += 1
newSpisok = [[0] * len(myDict) for i in range(len(spisok))]
for i in range(len(spisok)):
    for j in range(len(spisok[i])):
        newSpisok[i][myDict[spisok[i][j]]] += 1
matrix = np.array(newSpisok)
res = []
m1 = scipy.spatial.distance.cosine(matrix[0], matrix[1])
m2 = m1
ind1, ind2 = 0, 0
for i in range(1, len(matrix)):
    r = scipy.spatial.distance.cosine(matrix[0], matrix[i])
    if r < m1 or r < m2:
        if m1 < m2:
            m2 = r
            ind2 = i
        else:
            m1 = r
            ind1 = i
print(m1, m2, end = '', file = outFile)
