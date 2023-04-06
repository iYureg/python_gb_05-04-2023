text = "СъЕШЬ ещё этих МяГкИх французских булок"

print(len(text))
print('ещё' in text)
print(text.lower())
print(text.upper())
print(text.replace('ещё', 'ЕЩЁ'))

print(text[0])
print(text[1])
print(text[len(text) - 1])
print(text[-5])
print(text[:])
print(text[:2])
print(text[len(text) - 2:])
print(text[2:9])
print(text[6: -18])
print(text[0: len(text):6])
print(text[::6])
text = text[2:9] + text[-5] + text[:2]
print(text)