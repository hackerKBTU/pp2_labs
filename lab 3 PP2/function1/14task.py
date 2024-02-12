from palindrome import is_palindrome

word = input("Enter a word: ")
if is_palindrome(word):
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
