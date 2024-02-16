def div_three_four(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 ==0:
            yield i
for num in div_three_four(40):
    print(num)