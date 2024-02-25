import re

def snakeToCamel(text):
    camelCase = ""  # Corrected variable name
    pattern = re.compile(r"[_]")
    words = pattern.split(text)
    for i, word in enumerate(words):
        if i != 0:
            camelCase += word.capitalize()
        else:
            camelCase += word
    return camelCase
print(snakeToCamel("hello_world"))
