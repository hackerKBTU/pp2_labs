with open(r'C:\Users\Lenovo\Desktop\lab 6\demofile.txt', 'r') as file1, open(r"C:\\Users\\Lenovo\\Desktop\\demefile3.txt", 'a') as file2:
    for line in file1:
        file2.write(line)
