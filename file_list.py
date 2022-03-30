import os
file_path_list = []

for parent,dirnames,filenames in os.walk(path):
    for filename in filenames:
        if filename.lower().endswith('jpg'):
            file_path_list.append(os.path.join(parent,filename))
print(file_path_list)