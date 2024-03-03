from string import ascii_uppercase

for char in ascii_uppercase:
    file_path = r'C:\Users\Lenovo\Desktop\oibai\{fchar}.txt'.format(fchar=char)
    file = open(file_path, 'x')
    file.close()
