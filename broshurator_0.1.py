import os
import re


directory = '[IMG]'

list_movings = 0  #count number
log_moves = {}
if not os.path.isdir('.\\' + directory):
    os.mkdir('.\\' + directory)
for root, dirs, files in os.walk('.'):
    for file in files:
        if re.search(r'.+[.](jpg|png|jpeg|gif)', file.lower()) and os.stat(root + '\\' + file).st_size >150000 :
            print(root, file)
            os.replace(root + '\\' + file, '.\\' + directory + '\\'+ file)
            log_moves[file] = root + '\\' + file
            list_movings +=1
print(f'перемещено {list_movings} файлов изображений')
print(log_moves)
input(f'для продолжения нажмите на любую кнопку')

