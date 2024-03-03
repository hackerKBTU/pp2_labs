mylist = ['A', 'B', 'C', 'D','E']  # Defines a list containing four elements: 'A', 'B', 'C', 'D'

with open(r'C:\\Users\\Lenovo\\Desktop\\demofile2.txt', 'w') as file:  # Opens 'demofile2.txt' for writing
    for i in mylist:  # Iterates over each element in mylist
        file.write(i + '\n')  # Writes the current element followed by a newline character to the file
