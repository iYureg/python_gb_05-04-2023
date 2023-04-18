# Задача №25. Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

string = "a a a b c a a d c d d"
arr = string.split(" ")

dict = {}

for elem in range(len(arr)):
    if not arr[elem] in dict:
        dict[arr[elem]] = 0
        # print(dict)
    else:
        dict[arr[elem]] += 1
        arr[elem] += "_" + str(dict[arr[elem]])


print(*arr)
print("a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2")

# for i in range(len(arr)):
#     print(f"{arr[i]}_{arr[0:i].count(arr[i])}" if arr[0:i].count(
#         arr[i]) != 0 else string[i], end=" ")
