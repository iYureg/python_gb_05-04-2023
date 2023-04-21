# Задача №33. Найти факториал числа N
# N! = Nn * Nn-1 * Nn-2 ... до Nn=1

# input: 5
# output: 120

# Решить задачу с помощью рекурсии

def factor(n):
    if n == 1:
        return 1
    return n * factor(n-1)


mult = factor(5)

print(mult)
