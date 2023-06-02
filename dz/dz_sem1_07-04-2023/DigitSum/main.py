number = int(input('Введите число: '))

count = number
result = 0
while count:
    result += count % 10
    count //= 10

print(f"Cумма цифр числа {number} = {result}")

