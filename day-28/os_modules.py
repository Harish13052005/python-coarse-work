import os
import shutil

# os.makedirs('sample/demo')

path = os.path.join('sample/demo','demo.txt')
with open(path, 'w+') as file:
    file.write("Hello world")
    file.seek(0)
    print(file.read())

# rmdir(sample.txt) - used to delete empty folder
# shutil(.rmtree(sample.txt)) - to delete any folder
