# Задача №37.
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность во братном порядке.

# Примечание. В программе запрещается
# объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3


def reverseNums(n):
    if n == 0:
        return ""
    i = input("-> ")
    return reverseNums(n-1) + " " + i


print(reverseNums(5))
