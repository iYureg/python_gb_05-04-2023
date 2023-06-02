# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

min = int(input("Введите минимальное число: "))
max = int(input("Введите максимальное число: "))

from random import randint

rand_list = [randint(-10, 10) for i in range(30)]

def get_nums(small, big, array):
    res = []
    for index in range(len(array)):
        if small <= array[index] < big:
            res.append(index)
    return res

res_list = get_nums(min,max,rand_list)

print(rand_list)
print(res_list)