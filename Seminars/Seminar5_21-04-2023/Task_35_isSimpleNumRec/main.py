# Задача №35. Напишите функцию, которая принимает одно число и проверяет,
# является ли оно простым Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

# Input: 5
# Output: yes

n = int(input('-> '))


def check_simple(n, i=2):
    if n == i:
        return True
    elif n % i == 0:
        return False
    elif i * i > n:
        return True
    return check_simple(n, i + 1)


result = check_simple(n)
print(result)
