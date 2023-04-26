# Задача №43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел.
# Все числа списка находятся на разных строках.
#   Ввод:       Вывод:
# 1 2 3 2 3       2

lst = "11 4 1 2 3 11 2 3 1 4".split()

def count_couples3(array):
    res = 0
    for i in range(len(array)):
        res += array[i+1:].count(array[i])
    return res
print(count_couples3(lst))

def count_couples2(array):
    res = 0
    for item in set(array):
        res += array.count(item)//2
    return res
print(count_couples2(lst))


def count_couples(array):
    dt = {}
    res = 0
    for item in array:
        if item not in dt:
            dt[item] = 0
        elif item in dt and dt[item] == 0:
            dt[item] += 1
            res += dt[item]
    return res
print(count_couples(lst))

