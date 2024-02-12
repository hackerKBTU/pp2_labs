def wordRev():
    sentence = input("Enter a sentence: ")
    reversed_sentence = ' '.join(reversed(sentence.split()))
    print(reversed_sentence)

wordRev()
