import os
path = input("Enter Folder Path :>> ")
file = input("Enter File name :>> ")

file_name = os.path.join(path,file)

content = input("Enter Content to save:>> ")
with open(file_name,'w')as fw:
    fw.write(content)

with open(file_name,'r') as fr:
    read = fr.readline()
print(read)



