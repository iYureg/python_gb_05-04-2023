# Задача №23. Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

from random import randint

n = int(input("Введите размер массива: "))
arr = [ i * randint(-10, 10) for i in range(n)]
print(arr)

result = []

for i in range(len(arr) - 1):
    arr.append(arr.pop(0))
    if arr[0] > arr[-1]:
        result.append(arr[0])

arr.append(arr.pop(0))
print(len(result))

# count = 0
# for i in range(1, n):
#     if arr[i] > arr[i-1]:
#         count += 1   
    
# print(count)

    