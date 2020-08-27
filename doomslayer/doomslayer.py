import re

file_obj = open('sentences.txt')
strok = file_obj.read().lower()
spisok = re.split('[^a-z]', strok)
print(spisok)
