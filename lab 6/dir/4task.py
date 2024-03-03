with open(r'C:\\Users\\Lenovo\\Desktop\\demofile.txt', 'r') as file:
    x = len(file.readlines())
    print("Number of lines:", x)
