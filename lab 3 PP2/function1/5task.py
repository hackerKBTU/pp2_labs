def strPermut():
    word = input("Enter a word: ")
    perm = permutations(word)
    for i in list(perm):
        print(''.join(i))

strPermut()
