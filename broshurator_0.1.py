import os
import re
import sys


directory = '[IMG]'

if len(sys.argv) > 1:
    size_file = sys.argv[1]   # read file size from line
else:
    size_file = 500000

list_movings = 0  #count number
log_moves = {}
if not os.path.isdir('.\\' + directory):
    os.mkdir('.\\' + directory)
for root, dirs, files in os.walk('.'):
    [dirs.remove(d) for d in list(dirs) if d == directory]  # remove destination folder from waLK
    for file in files:
        if re.search(r'.+[.](jpg|png|jpeg|gif)', file.lower()) and os.stat(root + '\\' + file).st_size > size_file :
            print(root, file)
            os.replace(root + '\\' + file, '.\\' + directory + '\\'+ file)
            log_moves[file] = root + '\\' + file + ';'
            list_movings +=1
print(f'перемещено {list_movings} файлов изображений')
# print(log_moves)
print(size_file)
input(f'для продолжения нажмите на любую кнопку')

