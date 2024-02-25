import re

def camel_to_snake(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i == 0:
            res += word.casefold()
        else:
            res += "_" + word.casefold()
    return res

camel_case_string = "ThisIsASampleCamelCaseString"
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)
