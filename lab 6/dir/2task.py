import os

# Check if the path exists
print('Path exists:', os.access(r'C:\Users\Lenovo', os.F_OK))

# Check if the path is readable
print('Path readable:', os.access(r'C:\Users\Lenovo', os.R_OK))

# Check if the path is writable
print('Path writable:', os.access(r'C:\Users\Lenovo', os.W_OK))

# Check if the path is executable (this typically won't apply to directories on Windows)
print('Path executable:', os.access(r'C:\Users\Lenovo', os.X_OK))
