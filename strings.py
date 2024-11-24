def is_empty_or_blank(word):
    return word == ' '*len(word)

print(is_empty_or_blank('     '))

def starts_with(word,prefix):
    return word.startswith(prefix)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True