t = (1, 2, 3, 5,)
print(t[1])  # второй элемент кортежа - 2

print("------------------------------")

for i in t:
    print(i)

print("------------------------------")

for i in range(len(t)):
    print(f"index = {i} -> elem = {t[i]}")

# t[0] = 2 #### TypeError: 'tuple' object does not support item assignment
