def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for square in squares(1, 8):
    print(square)
