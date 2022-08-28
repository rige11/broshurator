import os
import re


directory = '[IMG]'

list_movings = 0
if not os.path.isdir('.\\' + directory):
    os.mkdir('.\\' + directory)
for root, dirs, files in os.walk('.'):
    for file in files:
        if re.search(r'.+[.]jpe*g', file.lower()) :
            print(root, file)
            os.replace(root + '\\' + file, '.\\' + directory + '\\'+ file)
            list_movings +=1
print(f'перемещено {list_movings} файлов изображений')
input(f'для продолжения нажмите на любую кнопку')
