import os

path = r"C:\\Users\\Lenovo\\Desktop\\testfile2.txt"
path_bool = os.access(path, os.F_OK)

if path_bool == False:
    print('Path does not exist')
elif path_bool == True:
    os.remove(path)
    print("File has been removed")
