# d = {}
# d = dict()
# d["q"] = "qwerty"
# print(d)

# print("----------------------")
# d["w"] = "werty"
# print(
#     f"ключ = 'q' значение = {d['q']}, ключ = 'w' значение = {d['w']}")

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# ← типы ключей могут отличаться
print(dictionary['left'])
# ↑ типы ключей могут отличаться
print(dictionary['up'])
dictionary['left'] = '⇐'
print(dictionary['left'])  # ⇐
# print(dictionary['type'])  # KeyError: 'type'
del dictionary['left']  # удаление элемента

print("___________________________")
for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))

print("___________________________")
for (key, value) in dictionary.items():
    print('{}: {}'.format(key, value))

print("___________________________")
print(dictionary.items())
