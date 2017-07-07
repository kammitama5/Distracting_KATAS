## Devise an algorithm to find only the second case of a word in a substring

substring = "zip"

a = text.find(substring)
b = text.find(substring, a+1)
c = text.find(substring, b+1)
print text.rfind(substring, b, len(text))