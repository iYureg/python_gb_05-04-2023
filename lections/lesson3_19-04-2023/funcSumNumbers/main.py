def sum_numbers(n, y='hello'):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa


result = sum_numbers(5, 'qwerty')

print(result)
