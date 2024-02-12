def isPal(word):
    return word == word[::-1]

word = input("Enter a word: ")

print(isPal(word))
