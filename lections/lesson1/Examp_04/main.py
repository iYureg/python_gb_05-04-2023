n = int(input())

flag = True
i = 2

while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делитель числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1

print('___________________')


a = 'qwerty'

for i in a:
    print(i)
    
print('___________________')

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "* "
    print(line)