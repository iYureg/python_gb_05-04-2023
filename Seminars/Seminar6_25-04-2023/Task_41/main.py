# Задача №41. Дан массив, состоящий из целых чисел. Напишите программу,
# которая в данном массиве определит количество элементов, у которых два соседних и,
# при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.
# Ввод:                         Ввод:
# 5                             5
# 1 2 3 4 5                     1 5 1 5 1
# Вывод:                        Вывод:
# 0                             2
# (каждое число вводится с новой строки)

lst_1 = "1 2 3 4 5".split()
lst_2 = "1 5 1 5 1 4 2 6 3 5 6".split()

def count_lower_neighbors(array):
    counter = 0
    for index in range(1, len(array) - 1):
        # if array[index-1] < array[index] and array[index] > array[index + 1]:
        if array[index -1] < array[index] > array[index + 1]:
            counter += 1
    return counter

print(count_lower_neighbors(lst_1))
print(count_lower_neighbors(lst_2))