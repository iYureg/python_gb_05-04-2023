# Задача No17. Решение в группахДан список чисел.
# Определите, сколько в немвстречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

from random import randint

n = int(input("Введите длину списка: "))

nSet = set()
nlist = []

for i in range(n):
    nlist.append(randint(-5, 5))
    nSet.add(nlist[i])

print(nlist)
print(f"В массиве {len(nSet)} уникальных значений -> {nSet}")


mList = [1, 1, 2, 0, -1, 3, 4, 4]
mSet = set(mList)
print(len(mSet))