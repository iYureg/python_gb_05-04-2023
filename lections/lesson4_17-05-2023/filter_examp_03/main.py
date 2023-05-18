# --- function filter ---

# метод filter принимает два парамета
# функцию с условием и объект с данными
# метод возвращает все элементы
# проходящие условие
#
data = [15, 65, 9, 36, 175]
print("data: ", data)
result = list(filter(lambda x: x % 10 == 5, data))
print("result: ", result)
