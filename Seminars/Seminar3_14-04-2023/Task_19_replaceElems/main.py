# Задача №19. Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


list_1 = [1,2,3,4,5,6,7,8,9]

n = int(input("Введите положительное число: "))
print(list_1)
if n > 0 and n < len(list_1):
    for i in range(n):
        list_1.append(list_1.pop(0))
    print(list_1)
elif n >= len(list_1):
    print("Слишком большое число")
else:
    print("Что непонятного в словах 'положительное число'?")

# print()
# list_2 = list_1[:n - 1] + list_1[n- 1:]
# print(list_2)