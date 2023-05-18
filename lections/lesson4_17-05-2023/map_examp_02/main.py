# --- функция map ---
list_1 = [x for x in range(1, 20)]
print("list_1: ", list_1)

# метод map принимает два аргумента
# функцию и объект с данными
# передаваемая функция будет пременена к каждому элементу передаваемого объекта
list_1 = list(map(lambda x: x + 10, list_1))
print("list_1: ", list_1)


# -----
data = "3 4 52 55 902 4 40 9 23 39 6"
print("data: ", data)
data = list(map(int, data.split()))
print("data: ", data)
