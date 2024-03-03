import os

# Specify the directory path
location1 = r'C:\Users\Lenovo'

# Print the list of all entries in the directory
print("all entries",[name for name in os.listdir(location1)])

# Print only the directories in the directory
print("only the directories",[name for name in os.listdir(location1) if os.path.isdir(os.path.join(location1, name))])

# Print only the files (non-directories) in the directory
print("only the files", [name for name in os.listdir(location1) if not os.path.isdir(os.path.join(location1, name))])


